from gem5.resources.resource import BinaryResource
from gem5.resources.workload import WorkloadResource

from pathlib import Path

_base_dir = Path(__file__).parent.absolute()

workloads = {
    "SVE_SAXPY": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/SVE_SAXPY/bench.gem5")
            )
        },
    ),
    "CRf": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CRf/bench.gem5")
            )
        },
    ),
    "CCh": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCh/bench.gem5")
            )
        },
    ),
    "MIP": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MIP/bench.gem5")
            )
        },
    ),
    "CCe": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCe/bench.gem5")
            )
        },
    ),
    "CCa": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCa/bench.gem5")
            )
        },
    ),
    "MIM2": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MIM2/bench.gem5")
            )
        },
    ),
    "DPT": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/DPT/bench.gem5")
            )
        },
    ),
    "ML2_st": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/ML2_st/bench.gem5")
            )
        },
    ),
    "EF": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/EF/bench.gem5")
            )
        },
    ),
    "MIM": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MIM/bench.gem5")
            )
        },
    ),
    "CS1": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CS1/bench.gem5")
            )
        },
    ),
    "CCl": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCl/bench.gem5")
            )
        },
    ),
    "STc": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/STc/bench.gem5")
            )
        },
    ),
    "DP1f": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/DP1f/bench.gem5")
            )
        },
    ),
    "STL2b": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/STL2b/bench.gem5")
            )
        },
    ),
    "CS3": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CS3/bench.gem5")
            )
        },
    ),
    "MD": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MD/bench.gem5")
            )
        },
    ),
    "DP1d": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/DP1d/bench.gem5")
            )
        },
    ),
    "ML2_BW_ld": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/ML2_BW_ld/bench.gem5")
            )
        },
    ),
    "STL2": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/STL2/bench.gem5")
            )
        },
    ),
    "M_Dyn": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/M_Dyn/bench.gem5")
            )
        },
    ),
    "EI": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/EI/bench.gem5")
            )
        },
    ),
    "EM1": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/EM1/bench.gem5")
            )
        },
    ),
    "MC": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MC/bench.gem5")
            )
        },
    ),
    "MI": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MI/bench.gem5")
            )
        },
    ),
    "CRm": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CRm/bench.gem5")
            )
        },
    ),
    "CCm": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCm/bench.gem5")
            )
        },
    ),
    "CF1": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CF1/bench.gem5")
            )
        },
    ),
    "ML2_BW_ldst": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/ML2_BW_ldst/bench.gem5")
            )
        },
    ),
    "MM": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MM/bench.gem5")
            )
        },
    ),
    "SVE_SUM": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/SVE_SUM/bench.gem5")
            )
        },
    ),
    "ML2": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/ML2/bench.gem5")
            )
        },
    ),
    "MM_st": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MM_st/bench.gem5")
            )
        },
    ),
    "MCS": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MCS/bench.gem5")
            )
        },
    ),
    "EM5": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/EM5/bench.gem5")
            )
        },
    ),
    "DPTd": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/DPTd/bench.gem5")
            )
        },
    ),
    "ML2_BW_st": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/ML2_BW_st/bench.gem5")
            )
        },
    ),
    "ED1": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/ED1/bench.gem5")
            )
        },
    ),
    "CRd": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CRd/bench.gem5")
            )
        },
    ),
    "DPcvt": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/DPcvt/bench.gem5")
            )
        },
    ),
    "CCh_st": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCh_st/bench.gem5")
            )
        },
    ),
    "CCa_aligned": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCa_aligned/bench.gem5")
            )
        },
    ),
    "CCe_aligned": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCe_aligned/bench.gem5")
            )
        },
    ),
    "CCh_aligned": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCh_aligned/bench.gem5")
            )
        },
    ),
    "CCh_st_aligned": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCh_st_aligned/bench.gem5")
            )
        },
    ),
    "CCl_aligned": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCl_aligned/bench.gem5")
            )
        },
    ),
    "CCm_aligned": WorkloadResource(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCm_aligned/bench.gem5")
            )
        },
    ),
}
