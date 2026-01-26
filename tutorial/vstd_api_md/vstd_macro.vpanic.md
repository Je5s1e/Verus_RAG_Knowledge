<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](index.html)

</div>

# Macro <span class="macro">vpanic</span> Copy item path

<span class="sub-heading"><a href="../src/vstd/pervasive.rs.html#463-476" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! vpanic {
    ($fmt:expr $(,$val:expr)*) => { ... };
    () => { ... };
}
```

Expand description

<div class="docblock">

Replace panic macro with vpanic when needed. panic!{} may call panic_fmt
with private rt::Argument, which could not be supported in verus.

</div>

</div>

</div>
