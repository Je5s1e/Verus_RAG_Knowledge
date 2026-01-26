<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[prelude](index.html)

</div>

# Macro <span class="macro">decreases_to</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_builtin/lib.rs.html#1862"
class="src">Source</a> </span>

</div>

``` rust
macro_rules! decreases_to {
    ($($x:tt)*) => { ... };
}
```

Expand description

<div class="docblock">

decreases_to!(b =\> a) means that height(a) \< height(b), so that b can
decrease to a in decreases clauses. decreases_to!(b1, …, bn =\> a1, …,
am) can compare lexicographically ordered values, which can be useful
when making assertions about decreases clauses. Notes:

- decreases_to! desugars to a call to is_smaller_than_lexicographic.
- you can write \#\[trigger\](decreases_to!(b =\> a)) to trigger on
  height(a). (in the SMT encoding, height is a function call and is a
  useful trigger, while is_smaller_than/is_smaller_than_lexicographic is
  not a function call and is not a useful trigger.)

</div>

</div>

</div>
