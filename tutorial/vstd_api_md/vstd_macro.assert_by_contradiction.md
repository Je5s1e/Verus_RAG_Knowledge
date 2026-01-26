<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](index.html)

</div>

# Macro <span class="macro">assert_by_contradiction</span> Copy item path

<span class="sub-heading"><a href="../src/vstd/pervasive.rs.html#233-237" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! assert_by_contradiction {
    ($($a:tt)*) => { ... };
}
```

Expand description

<div class="docblock">

Allows you to prove a boolean predicate by assuming its negation and
proving a contradiction.

`assert_by_contradiction!(b, { /* proof */ });` Equivalent to writing
`if !b { /* proof */; assert(false); }` but is more concise and
documents intent.

<div class="example-wrap">

``` rust
assert_by_contradiction!(b, {
    // assume !b here
    // prove `false`
});
```

</div>

</div>

</div>

</div>
