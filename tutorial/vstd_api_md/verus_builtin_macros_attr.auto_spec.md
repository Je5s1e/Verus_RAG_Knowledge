<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_builtin_macros](index.html)

</div>

# Attribute Macro <span class="attr">auto_spec</span> Copy item path

<span class="sub-heading"><a href="../src/verus_builtin_macros/lib.rs.html#417-423"
class="src">Source</a> </span>

</div>

``` rust
#[auto_spec]
```

Expand description

<div class="docblock">

This copies the body of an exec function into a “returns” clause, so
that the exec function will be also usable as a spec function. For
example, `#[vstd::contrib::auto_spec] fn f(u: u8) -> u8 { u / 2 }`
becomes:
`#[verifier::allow_in_spec] fn f(u: u8) -> u8 returns (u / 2) { u / 2 }`
The macro performs some limited fixups, such as removing proof blocks
and turning +, -, and \* into add, sub, mul. However, only a few such
fixups are currently implemented and not all exec bodies will be usable
as return clauses, so this macro will not work on all exec functions.

</div>

</div>

</div>
