from typing import Union


class FSCommandWrapper:
    def __init__(self, binary_path: str):
        self._binary_path = binary_path

    def generate_cmdline(self):
        raise NotImplementedError

    def generate_id_dict(self):
        raise NotImplementedError


class BransonCommandWrapper(FSCommandWrapper):
    input_translator = {
        "hohlraum_single": "3D_hohlraum_multi_node",
        "hohlraum_multi": "3D_hohlraum_multi_node",
    }

    def __init__(self, input_name: str):
        super().__init__("/home/ubuntu/benchmarks/branson/build/BRANSON")
        self._input_name = BransonCommandWrapper.input_translator[input_name]
        self._input_path = (
            f"/home/ubuntu/benchmarks/branson/inputs/{self._input_name}.xml"
        )

    def generate_cmdline(self):
        return f"{self._binary_path} {self._input_path}"

    def generate_id_dict(self):
        return {"name": "branson", "input": self._input_name}


class NPBCommandWrapper(FSCommandWrapper):
    def __init__(self, workload: str, size: str):
        self._workload = workload
        self._size = size
        binary_name = f"{workload}.{size}.x"
        super().__init__(
            f"/home/ubuntu/benchmarks/NPB3.4-OMP/bin/{binary_name}"
        )

    def generate_cmdline(self):
        return f"{self._binary_path}"

    def generate_id_dict(self):
        return {"name": "npb", "workload": self._workload, "size": self._size}


class SimpleVectorWrapper(FSCommandWrapper):
    def __init__(self, binary_path: str, use_sve: Union[bool, str]):
        def try_convert_bool(bool_like):
            def convert_str_bool(bool_like):
                assert bool_like.lower() in ["true", "false"]
                return True if bool_like.lower() == "true" else False

            def is_int_like(int_like):
                try:
                    ret = int(int_like)
                    return True
                except:
                    return False

            def convert_int_bool(bool_like):
                assert bool_like >= 0
                return bool_like > 0

            if isinstance(bool_like, str):
                if is_int_like(bool_like):
                    return convert_int_bool(bool_like)
                else:
                    return convert_str_bool(bool_like)
            elif isinstance(bool_like, int):
                return convert_int_bool(bool_like)
            elif isinstance(bool_like, bool):
                return bool_like
            else:
                raise ValueError(
                    "bool_like argument should be a string/positive integer/boolean."
                )

        self._processing_mode = (
            "sve" if try_convert_bool(use_sve) else "scalar"
        )
        suffix = "-sve.gem5" if try_convert_bool(use_sve) else ".gem5"
        super().__init__(binary_path + suffix)


class GUPSCommandWrapper(SimpleVectorWrapper):
    def __init__(
        self,
        num_elements: int,
        updates_per_burst: int,
        use_sve: Union[bool, str],
    ):
        super().__init__(
            "/home/ubuntu/benchmarks/simple-vector-bench/gups/bin/gups",
            use_sve,
        )
        self._num_elements = num_elements
        self._updates_per_burst = updates_per_burst

    def generate_cmdline(self):
        return f"{self._binary_path} {self._num_elements} {self._updates_per_burst}"

    def generate_id_dict(self):
        return {
            "name": "gups",
            "processing_mode": self._processing_mode,
            "num_elements": self._num_elements,
            "updates_per_burst": self._updates_per_burst,
        }


class PermutatingGatherCommandWrapper(SimpleVectorWrapper):
    def __init__(self, seed: int, mod: int, use_sve: Union[bool, str]):
        super().__init__(
            "/home/ubuntu/benchmarks/simple-vector-bench/permutating-gather/bin/permutating-gather",
            use_sve,
        )
        self._seed = seed
        self._mod = mod

    def generate_cmdline(self):
        return f"{self._binary_path} {self._seed} {self._mod}"

    def generate_id_dict(self):
        return {
            "name": "permutating-gather",
            "processing_mode": self._processing_mode,
            "seed": self._seed,
            "mod": self._mod,
        }


class PermutatingScatterCommandWrapper(SimpleVectorWrapper):
    def __init__(self, seed: int, mod: int, use_sve: Union[bool, str]):
        super().__init__(
            "/home/ubuntu/benchmarks/simple-vector-bench/permutating-scatter/bin/permutating-scatter",
            use_sve,
        )
        self._seed = seed
        self._mod = mod

    def generate_cmdline(self):
        return f"{self._binary_path} {self._seed} {self._mod}"

    def generate_id_dict(self):
        return {
            "name": "permutating-scatter",
            "processing_mode": self._processing_mode,
            "seed": self._seed,
            "mod": self._mod,
        }


class SpatterCommandWrapper(SimpleVectorWrapper):
    def __init__(self, json_file_path: str, use_sve: Union[bool, str]):
        super().__init__(
            "/home/ubuntu/benchmarks/simple-vector-bench/spatter/bin/spatter",
            use_sve,
        )
        self._json_file_loc = json_file_path
        self._json_file_path = f"/home/ubuntu/benchmarks/simple-vector-bench/spatter/patterns/{json_file_path}"

    def generate_cmdline(self):
        return f"{self._binary_path} {self._json_file_path}"

    def generate_id_dict(self):
        return {
            "name": "spatter",
            "processing_mode": self._processing_mode,
            "json_file_loc": self._json_file_loc,
        }


class StreamCommandWrapper(SimpleVectorWrapper):
    def __init__(self, array_size, use_sve: Union[bool, str]):
        super().__init__(
            "/home/ubuntu/benchmarks/simple-vector-bench/stream/bin/stream",
            use_sve,
        )
        self._array_size = array_size

    def generate_cmdline(self):
        return f"{self._binary_path} {self._array_size}"

    def generate_id_dict(self):
        return {
            "name": "stream",
            "processing_mode": self._processing_mode,
            "array_size": self._array_size,
        }
