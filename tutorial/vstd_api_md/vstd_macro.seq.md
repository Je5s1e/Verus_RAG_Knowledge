<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](index.html)

</div>

# Macro <span class="macro">seq</span> Copy item path

<span class="sub-heading"><a href="../src/vstd/seq.rs.html#546-550" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! seq {
    [$($tail:tt)*] => { ... };
}
```

Expand description

<div class="docblock">

Creates a [`Seq`](seq/struct.Seq.html "struct vstd::seq::Seq")
containing the given elements.

### <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
let s = seq![11int, 12, 13];

assert(s.len() == 3);
assert(s[0] == 11);
assert(s[1] == 12);
assert(s[2] == 13);
```

</div>

</div>

</div>

</div>
