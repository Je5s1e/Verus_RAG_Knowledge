<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

# Crate hashbrown Copy item path

<span class="sub-heading"><a href="../src/hashbrown/lib.rs.html#1-150" class="src">Source</a>
</span>

</div>

Expand description

<div class="docblock">

This crate is a Rust port of Google’s high-performance
[SwissTable](https://abseil.io/blog/20180927-swisstables) hash map,
adapted to make it a drop-in replacement for Rust’s standard `HashMap`
and `HashSet` types.

The original C++ version of
[SwissTable](https://abseil.io/blog/20180927-swisstables) can be found
[here](https://github.com/abseil/abseil-cpp/blob/master/absl/container/internal/raw_hash_set.h),
and this [CppCon talk](https://www.youtube.com/watch?v=ncHmEUmJZf4)
gives an overview of how the algorithm works.

</div>

## Modules<a href="#modules" class="anchor">§</a>

<a href="hash_map/index.html" class="mod"
title="mod hashbrown::hash_map">hash_map</a>  
A hash map implemented with quadratic probing and SIMD lookup.

<a href="hash_set/index.html" class="mod"
title="mod hashbrown::hash_set">hash_set</a>  
A hash set implemented as a `HashMap` where the value is `()`.

<a href="raw/index.html" class="mod" title="mod hashbrown::raw">raw</a>  
Experimental and unsafe `RawTable` API. This module is only available if
the `raw` feature is enabled.

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>  
A hash map implemented with quadratic probing and SIMD lookup.

<a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>  
A hash set implemented as a `HashMap` where the value is `()`.

## Enums<a href="#enums" class="anchor">§</a>

<a href="enum.TryReserveError.html" class="enum"
title="enum hashbrown::TryReserveError">TryReserveError</a>  
The error type for `try_reserve` methods.

</div>

</div>
