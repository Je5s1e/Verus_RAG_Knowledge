<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[indexmap](index.html)

</div>

# Macro <span class="macro">indexmap</span> Copy item path

<span class="sub-heading"><a href="../src/indexmap/macros.rs.html#21-36" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! indexmap {
    (@single $($x:tt)*) => { ... };
    (@count $($rest:expr),*) => { ... };
    ($($key:expr => $value:expr,)+) => { ... };
    ($($key:expr => $value:expr),*) => { ... };
}
```

Expand description

<div class="docblock">

Create an `IndexMap` from a list of key-value pairs

### <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use indexmap::indexmap;

let map = indexmap!{
    "a" => 1,
    "b" => 2,
};
assert_eq!(map["a"], 1);
assert_eq!(map["b"], 2);
assert_eq!(map.get("c"), None);

// "a" is the first key
assert_eq!(map.keys().next(), Some(&"a"));
```

</div>

</div>

</div>

</div>
