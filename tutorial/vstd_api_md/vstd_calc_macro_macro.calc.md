<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[calc_macro](index.html)

</div>

# Macro <span class="macro">calc</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/calc_macro.rs.html#50-54" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! calc {
    ($($tt:tt)*) => { ... };
}
```

Expand description

<div class="docblock">

The `calc!` macro supports structured proofs through calculations.

In particular, one can show `a_1 R a_n` for some transitive relation `R`
by performing a series of steps `a_1 R a_2`, `a_2 R a_3`, …
`a_{n-1} R a_n`. The calc macro provides both convenient syntax sugar to
perform such a proof conveniently, without repeating oneself too often,
or exposing the internal steps to the outside context.

The expected usage looks like:

<div class="example-wrap">

``` rust
calc! {
  (R)
  a_1; { /* proof that a_1 R a_2 */ }
  a_2; { /* proof that a_2 R a_3 */ }
   ...
  a_n;
}
```

</div>

Currently, the `calc!` macro supports common transitive relations for
`R`, and this set of relations may be extended in the future.

Note that `calc!` also supports stating intermediate relations, as long
as they are consistent with the main relation `R`. If consistency cannot
be immediately shown, Verus will give a helpful message about this.
Intermediate relations can be specified by placing them right before the
proof block of that step.

A simple example of using intermediate relations looks like:

<div class="example-wrap">

``` rust
let x: int = 2;
let y: int = 5;
calc! {
  (<=)
  x; (==) {}
  5 - 3; (<) {}
  5; {} // Notice that no intermediate relation is specified here, so `calc!` will consider the top-level relation `R`; here `<=`.
  y;
}
```

</div>

</div>

</div>

</div>
