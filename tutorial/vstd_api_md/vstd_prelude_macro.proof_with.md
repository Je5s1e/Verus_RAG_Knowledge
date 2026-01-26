<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[prelude](index.html)

</div>

# Macro <span class="macro">proof_with</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_builtin_macros/lib.rs.html#355"
class="src">Source</a> </span>

</div>

``` rust
proof_with!() { /* proc-macro */ }
```

Expand description

<div class="docblock">

proof_with add ghost input/output to the next function call. In stable
rust, we cannot add attribute-based macro to expr/statement. Using
proof_with! to tell \#\[verus_spec\] to add ghost input/output. Using
proof_with outside of \#\[verus_spec\] does not have any side effects.

</div>

</div>

</div>
