from pathlib import Path


def _c_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def generate_c(game_name, players, strategies, payoffs, compute, out_path="generated_game.c"):
    n = len(players)

    strat_lists = []
    strat_index = []
    for p in players:
        sl = sorted(list(strategies.get(p, [])))
        strat_lists.append(sl)
        strat_index.append({name: i for i, name in enumerate(sl)})

    payoff_entries = []
    for prof, utils in payoffs:
        prof_idx = []
        for i, sname in enumerate(prof):
            if sname not in strat_index[i]:
                raise ValueError(f"Strategy '{sname}' not defined for player '{players[i]}'")
            prof_idx.append(strat_index[i][sname])
        payoff_entries.append((prof_idx, utils))

    players_c = ",\n    ".join([f"\"{_c_escape(p)}\"" for p in players])

    strat_arrays_c = []
    strat_ptrs = []
    strat_counts = []
    for i, sl in enumerate(strat_lists):
        arr = ", ".join([f"\"{_c_escape(s)}\"" for s in sl])
        strat_arrays_c.append(f"static const char* STRATS_P{i}[{len(sl)}] = {{ {arr} }};")
        strat_ptrs.append(f"STRATS_P{i}")
        strat_counts.append(len(sl))

    strat_ptrs_c = ", ".join(strat_ptrs)
    strat_counts_c = ", ".join(map(str, strat_counts))

    payoff_c_lines = []
    for prof_idx, utils in payoff_entries:
        payoff_c_lines.append(
            f"    {{ {{ {', '.join(map(str, prof_idx))} }}, {{ {', '.join(map(str, utils))} }} }},"
        )
    payoff_c_block = "\n".join(payoff_c_lines) if payoff_c_lines else "    /* empty */"

    code = f"""\

#include <stdio.h>
#include <string.h>

#define N_PLAYERS {n}
#define N_PAYOFFS {len(payoff_entries)}

static const char* GAME_NAME = "{_c_escape(game_name)}";
static const char* PLAYERS[N_PLAYERS] = {{
    {players_c}
}};

{chr(10).join(strat_arrays_c)}

static const char** STRATS[N_PLAYERS] = {{ {strat_ptrs_c} }};
static const int STRAT_COUNTS[N_PLAYERS] = {{ {strat_counts_c} }};

typedef struct {{
    int profile[N_PLAYERS];  
    int util[N_PLAYERS];     
}} PayoffEntry;

static const PayoffEntry PAYOFFS[N_PAYOFFS] = {{
{payoff_c_block}
}};

static const char* COMPUTE = "{_c_escape(compute)}";

static int profiles_equal(const int a[N_PLAYERS], const int b[N_PLAYERS]) {{
    for (int i = 0; i < N_PLAYERS; i++) {{
        if (a[i] != b[i]) return 0;
    }}
    return 1;
}}

static const PayoffEntry* find_payoff(const int profile[N_PLAYERS]) {{
    for (int i = 0; i < N_PAYOFFS; i++) {{
        if (profiles_equal(PAYOFFS[i].profile, profile)) {{
            return &PAYOFFS[i];
        }}
    }}
    return NULL;
}}

static void print_profile(const int profile[N_PLAYERS]) {{
    printf("(");
    for (int i = 0; i < N_PLAYERS; i++) {{
        const char* sname = STRATS[i][ profile[i] ];
        printf("%s", sname);
        if (i != N_PLAYERS - 1) printf(", ");
    }}
    printf(")");
}}

static void print_util(const int util[N_PLAYERS]) {{
    printf("(");
    for (int i = 0; i < N_PLAYERS; i++) {{
        printf("%d", util[i]);
        if (i != N_PLAYERS - 1) printf(", ");
    }}
    printf(")");
}}

static void show_matrix(void) {{
    printf("\\nPayoffs:\\n");
    for (int i = 0; i < N_PAYOFFS; i++) {{
        print_profile(PAYOFFS[i].profile);
        printf(" -> ");
        print_util(PAYOFFS[i].util);
        printf("\\n");
    }}
}}

static void best_responses(void) {{
    printf("\\nBest Responses:\\n");

    for (int i = 0; i < N_PLAYERS; i++) {{
        for (int base_idx = 0; base_idx < N_PAYOFFS; base_idx++) {{

            // compute best replies for player i given others fixed as in PAYOFFS[base_idx]
            int best_u = 0;
            int has_best = 0;

            int best_strats[256];
            int best_count = 0;

            for (int j = 0; j < N_PAYOFFS; j++) {{
                // match others
                int match = 1;
                for (int k = 0; k < N_PLAYERS; k++) {{
                    if (k == i) continue;
                    if (PAYOFFS[j].profile[k] != PAYOFFS[base_idx].profile[k]) {{
                        match = 0;
                        break;
                    }}
                }}
                if (!match) continue;

                int u = PAYOFFS[j].util[i];
                if (!has_best || u > best_u) {{
                    best_u = u;
                    has_best = 1;
                    best_count = 0;
                    best_strats[best_count++] = PAYOFFS[j].profile[i];
                }} else if (u == best_u) {{
                    // avoid duplicates
                    int sidx = PAYOFFS[j].profile[i];
                    int dup = 0;
                    for (int t = 0; t < best_count; t++) {{
                        if (best_strats[t] == sidx) {{ dup = 1; break; }}
                    }}
                    if (!dup) best_strats[best_count++] = sidx;
                }}
            }}

            printf("Player %s given others=(", PLAYERS[i]);
            for (int k = 0; k < N_PLAYERS; k++) {{
                if (k == i) continue;
                printf("%s", STRATS[k][ PAYOFFS[base_idx].profile[k] ]);

                // comma between other players
                int is_last_other = 1;
                for (int kk = k + 1; kk < N_PLAYERS; kk++) {{
                    if (kk != i) {{ is_last_other = 0; break; }}
                }}
                if (!is_last_other) printf(", ");
            }}
            printf(") -> best={{");
            for (int t = 0; t < best_count; t++) {{
                printf("%s", STRATS[i][ best_strats[t] ]);
                if (t != best_count - 1) printf(", ");
            }}
            printf("}}\\n");
        }}
        printf("\\n");
    }}
}}

static int is_nash_profile(const int profile[N_PLAYERS]) {{
    const PayoffEntry* pe = find_payoff(profile);
    if (!pe) return 0;

    for (int i = 0; i < N_PLAYERS; i++) {{
        int current_u = pe->util[i];

        for (int s = 0; s < STRAT_COUNTS[i]; s++) {{
            if (s == profile[i]) continue;

            int alt[N_PLAYERS];
            for (int k = 0; k < N_PLAYERS; k++) alt[k] = profile[k];
            alt[i] = s;

            const PayoffEntry* alt_pe = find_payoff(alt);
            if (!alt_pe) continue;

            if (alt_pe->util[i] > current_u) {{
                return 0;
            }}
        }}
    }}
    return 1;
}}

static void nash(void) {{
    printf("\\nNash Equilibrium:\\n");
    int found = 0;
    for (int i = 0; i < N_PAYOFFS; i++) {{
        if (is_nash_profile(PAYOFFS[i].profile)) {{
            print_profile(PAYOFFS[i].profile);
            printf("\\n");
            found = 1;
        }}
    }}
    if (!found) {{
        printf("None found (No pure strategy equilibrium)\\n");
    }}
}}

int main(void) {{
    printf("Game: %s\\n", GAME_NAME);

    if (strcmp(COMPUTE, "Nash") == 0 || strcmp(COMPUTE, "BestResponses") == 0) {{
        int expected = 1;
        for (int i = 0; i < N_PLAYERS; i++) expected *= STRAT_COUNTS[i];
        if (expected != N_PAYOFFS) {{
            printf("Warning: Missing payoff entries. Expected %d, found %d.\\n", expected, N_PAYOFFS);
        }}
    }}

    if (strcmp(COMPUTE, "ShowMatrix") == 0) {{
        show_matrix();
    }} else if (strcmp(COMPUTE, "BestResponses") == 0) {{
        best_responses();
    }} else if (strcmp(COMPUTE, "Nash") == 0) {{
        nash();
    }} else {{
        printf("Unknown compute: %s\\n", COMPUTE);
    }}

    return 0;
}}
"""

    Path(out_path).write_text(code, encoding="utf-8")
    return out_path
