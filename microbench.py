from gem5.resources.resource import BinaryResource
from gem5.resources.workload import CustomWorkload

from pathlib import Path

_base_dir = Path(__file__).parent.absolute()

workloads = {
    "SVE_SAXPY": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/SVE_SAXPY/bench.gem5")
            )
        },
    ),
    "CRf": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CRf/bench.gem5")
            )
        },
    ),
    "CCh": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCh/bench.gem5")
            )
        },
    ),
    "MIP": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MIP/bench.gem5")
            )
        },
    ),
    "CCe": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCe/bench.gem5")
            )
        },
    ),
    "CCa": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCa/bench.gem5")
            )
        },
    ),
    "MIM2": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MIM2/bench.gem5")
            )
        },
    ),
    "DPT": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/DPT/bench.gem5")
            )
        },
    ),
    "ML2_st": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/ML2_st/bench.gem5")
            )
        },
    ),
    "EF": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/EF/bench.gem5")
            )
        },
    ),
    "MIM": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MIM/bench.gem5")
            )
        },
    ),
    "CS1": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CS1/bench.gem5")
            )
        },
    ),
    "CCl": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCl/bench.gem5")
            )
        },
    ),
    "STc": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/STc/bench.gem5")
            )
        },
    ),
    "DP1f": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/DP1f/bench.gem5")
            )
        },
    ),
    "STL2b": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/STL2b/bench.gem5")
            )
        },
    ),
    "CS3": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CS3/bench.gem5")
            )
        },
    ),
    "MD": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MD/bench.gem5")
            )
        },
    ),
    "DP1d": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/DP1d/bench.gem5")
            )
        },
    ),
    "ML2_BW_ld": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/ML2_BW_ld/bench.gem5")
            )
        },
    ),
    "STL2": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/STL2/bench.gem5")
            )
        },
    ),
    "M_Dyn": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/M_Dyn/bench.gem5")
            )
        },
    ),
    "EI": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/EI/bench.gem5")
            )
        },
    ),
    "EM1": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/EM1/bench.gem5")
            )
        },
    ),
    "MC": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MC/bench.gem5")
            )
        },
    ),
    "MI": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MI/bench.gem5")
            )
        },
    ),
    "CRm": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CRm/bench.gem5")
            )
        },
    ),
    "CCm": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCm/bench.gem5")
            )
        },
    ),
    "CF1": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CF1/bench.gem5")
            )
        },
    ),
    "ML2_BW_ldst": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/ML2_BW_ldst/bench.gem5")
            )
        },
    ),
    "MM": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MM/bench.gem5")
            )
        },
    ),
    "SVE_SUM": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/SVE_SUM/bench.gem5")
            )
        },
    ),
    "ML2": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/ML2/bench.gem5")
            )
        },
    ),
    "MM_st": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MM_st/bench.gem5")
            )
        },
    ),
    "MCS": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/MCS/bench.gem5")
            )
        },
    ),
    "EM5": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/EM5/bench.gem5")
            )
        },
    ),
    "DPTd": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/DPTd/bench.gem5")
            )
        },
    ),
    "ML2_BW_st": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/ML2_BW_st/bench.gem5")
            )
        },
    ),
    "ED1": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/ED1/bench.gem5")
            )
        },
    ),
    "CRd": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CRd/bench.gem5")
            )
        },
    ),
    "DPcvt": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/DPcvt/bench.gem5")
            )
        },
    ),
    "CCh_st": CustomWorkload(
        function="set_se_binary_workload",
        parameters={
            "binary": BinaryResource(
                str(_base_dir / "microbench/CCh_st/bench.gem5")
            )
        },
    ),
}
