<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

# Crate indexmap Copy item path

<span class="sub-heading"><a href="../src/indexmap/lib.rs.html#2-194" class="src">Source</a>
</span>

</div>

Expand description

<div class="docblock">

[`IndexMap`](map/struct.IndexMap.html) is a hash table where the
iteration order of the key-value pairs is independent of the hash values
of the keys.

[`IndexSet`](set/struct.IndexSet.html) is a corresponding hash set using
the same implementation and with similar properties.

#### <a href="#feature-highlights" class="doc-anchor">§</a>Feature Highlights

[`IndexMap`](map/struct.IndexMap.html) and
[`IndexSet`](set/struct.IndexSet.html) are drop-in compatible with the
std `HashMap` and `HashSet`, but they also have some features of note:

- The ordering semantics (see their documentation for details)
- Sorting methods and the
  [`.pop()`](map/struct.IndexMap.html#method.pop "method indexmap::map::IndexMap::pop")
  methods.
- The [`Equivalent`](trait.Equivalent.html "trait indexmap::Equivalent")
  trait, which offers more flexible equality definitions between
  borrowed and owned versions of keys.
- The
  [`MutableKeys`](map/trait.MutableKeys.html "trait indexmap::map::MutableKeys")
  trait, which gives opt-in mutable access to hash map keys.

#### <a href="#alternate-hashers" class="doc-anchor">§</a>Alternate Hashers

[`IndexMap`](map/struct.IndexMap.html) and
[`IndexSet`](set/struct.IndexSet.html) have a default hasher type
`S = RandomState`, just like the standard `HashMap` and `HashSet`, which
is resistant to HashDoS attacks but not the most performant. Type
aliases can make it easier to use alternate hashers:

<div class="example-wrap">

``` rust
use fnv::FnvBuildHasher;
use fxhash::FxBuildHasher;
use indexmap::{IndexMap, IndexSet};

type FnvIndexMap<K, V> = IndexMap<K, V, FnvBuildHasher>;
type FnvIndexSet<T> = IndexSet<T, FnvBuildHasher>;

type FxIndexMap<K, V> = IndexMap<K, V, FxBuildHasher>;
type FxIndexSet<T> = IndexSet<T, FxBuildHasher>;

let std: IndexSet<i32> = (0..100).collect();
let fnv: FnvIndexSet<i32> = (0..100).collect();
let fx: FxIndexSet<i32> = (0..100).collect();
assert_eq!(std, fnv);
assert_eq!(std, fx);
```

</div>

#### <a href="#rust-version" class="doc-anchor">§</a>Rust Version

This version of indexmap requires Rust 1.56 or later.

The indexmap 1.x release series will use a carefully considered version
upgrade policy, where in a later 1.x version, we will raise the minimum
required Rust version.

### <a href="#no-standard-library-targets" class="doc-anchor">§</a>No Standard Library Targets

This crate supports being built without `std`, requiring `alloc`
instead. This is enabled automatically when it is detected that `std` is
not available. There is no crate feature to enable/disable to trigger
this. It can be tested by building for a std-less target.

- Creating maps and sets using
  [`new`](map/struct.IndexMap.html#method.new "associated function indexmap::map::IndexMap::new")
  and
  [`with_capacity`](map/struct.IndexMap.html#method.with_capacity "associated function indexmap::map::IndexMap::with_capacity")
  is unavailable without `std`.  
  Use methods
  [`IndexMap::default`](map/struct.IndexMap.html#impl-Default),
  [`with_hasher`](map/struct.IndexMap.html#method.with_hasher "associated function indexmap::map::IndexMap::with_hasher"),
  [`with_capacity_and_hasher`](map/struct.IndexMap.html#method.with_capacity_and_hasher "associated function indexmap::map::IndexMap::with_capacity_and_hasher")
  instead. A no-std compatible hasher will be needed as well, for
  example from the crate `twox-hash`.
- Macros [`indexmap!`](macro.indexmap.html "macro indexmap::indexmap")
  and [`indexset!`](macro.indexset.html "macro indexmap::indexset") are
  unavailable without `std`.

</div>

## Re-exports<a href="#reexports" class="anchor">§</a>

`pub use crate::map::`<a href="map/struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap"><code>IndexMap</code></a>`;`

`pub use crate::set::`<a href="set/struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet"><code>IndexSet</code></a>`;`

## Modules<a href="#modules" class="anchor">§</a>

<a href="map/index.html" class="mod" title="mod indexmap::map">map</a>  
`IndexMap` is a hash table where the iteration order of the key-value
pairs is independent of the hash values of the keys.

<a href="set/index.html" class="mod" title="mod indexmap::set">set</a>  
A hash set implemented using `IndexMap`

## Macros<a href="#macros" class="anchor">§</a>

<a href="macro.indexmap.html" class="macro"
title="macro indexmap::indexmap">indexmap</a>  
Create an `IndexMap` from a list of key-value pairs

<a href="macro.indexset.html" class="macro"
title="macro indexmap::indexset">indexset</a>  
Create an `IndexSet` from a list of values

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>  
Key equivalence trait.

</div>

</div>
