<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[map](index.html)

</div>

# Macro <span class="macro">map</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/map.rs.html#328-332" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! map {
    [$($tail:tt)*] => { ... };
}
```

Expand description

<div class="docblock">

Create a map using syntax like `map![key1 => val1, key2 => val, ...]`.

This is equivalent to
`Map::empty().insert(key1, val1).insert(key2, val2)...`.

Note that this does *not* require all keys to be distinct. In the case
that two or more keys are equal, the resulting map uses the value of the
rightmost entry.

</div>

</div>

</div>
