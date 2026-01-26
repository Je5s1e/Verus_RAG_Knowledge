<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[layout](index.html)

</div>

# Function <span class="fn">layout_for_type_is_valid</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/layout.rs.html#88-98" class="src">Source</a>
</span>

</div>

``` rust
pub fn layout_for_type_is_valid<V>()
```

Expand description

<div class="docblock">

Lemma to learn that the (size, alignment) of a type is a valid “layout”.
See \[`valid_layout`\] for the exact conditions.

Also exports that size is a multiple of alignment
([Reference](https://doc.rust-lang.org/reference/type-layout.html#r-layout.properties.size)).

Note that, unusually for a lemma, this is an `exec`-mode function. (This
is necessary to ensure that the types are really compilable, as ghost
code can reason about “virtual” types that exceed these bounds.) Despite
being `exec`-mode, it is a no-op.

</div>

</div>

</div>
