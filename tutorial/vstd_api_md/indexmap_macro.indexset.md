<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[indexmap](index.html)

</div>

# Macro <span class="macro">indexset</span> Copy item path

<span class="sub-heading"><a href="../src/indexmap/macros.rs.html#58-73" class="src">Source</a>
</span>

</div>

``` rust
macro_rules! indexset {
    (@single $($x:tt)*) => { ... };
    (@count $($rest:expr),*) => { ... };
    ($($value:expr,)+) => { ... };
    ($($value:expr),*) => { ... };
}
```

Expand description

<div class="docblock">

Create an `IndexSet` from a list of values

### <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
use indexmap::indexset;

let set = indexset!{
    "a",
    "b",
};
assert!(set.contains("a"));
assert!(set.contains("b"));
assert!(!set.contains("c"));

// "a" is the first value
assert_eq!(set.iter().next(), Some(&"a"));
```

</div>

</div>

</div>

</div>
