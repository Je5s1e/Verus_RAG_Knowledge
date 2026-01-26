<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[prelude](index.html)

</div>

# Macro <span class="macro">verus_proof_macro_explicit_exprs</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_builtin_macros/lib.rs.html#308"
class="src">Source</a> </span>

</div>

``` rust
verus_proof_macro_explicit_exprs!() { /* proc-macro */ }
```

Expand description

<div class="docblock">

`verus_proof_macro_explicit_exprs!(f!(tts))` applies verus syntax to
transform `tts` into `tts'`, then returns `f!(tts')`, only applying the
transform to any of the exprs within it that are explicitly prefixed
with `@@`, leaving the rest as-is. Contrast this to
\[`verus_proof_macro_exprs`\] which is likely what you want to try first
to see if it satisfies your needs.

</div>

</div>

</div>
