<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_builtin_macros](index.html)

</div>

# Macro <span class="macro">proof_decl</span> Copy item path

<span class="sub-heading"><a href="../src/verus_builtin_macros/lib.rs.html#371-378"
class="src">Source</a> </span>

</div>

``` rust
proof_decl!() { /* proc-macro */ }
```

Expand description

<div class="docblock">

proof_decl add extra stmts that are used only for verification. For
example, declare a ghost/tracked variable. To avoid confusion, let stmts
without ghost/tracked is not supported. Non-local stmts inside
proof_decl! are treated similar to those in proof!

</div>

</div>

</div>
