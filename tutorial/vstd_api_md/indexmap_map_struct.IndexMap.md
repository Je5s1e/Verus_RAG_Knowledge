<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[indexmap](../index.html)::[map](index.html)

</div>

# Struct <span class="struct">IndexMap</span> Copy item path

<span class="sub-heading"><a href="../../src/indexmap/map.rs.html#71-74" class="src">Source</a>
</span>

</div>

``` rust
pub struct IndexMap<K, V, S = RandomState> { /* private fields */ }
```

Expand description

<div class="docblock">

A hash table where the iteration order of the key-value pairs is
independent of the hash values of the keys.

The interface is closely compatible with the standard `HashMap`, but
also has additional features.

## <a href="#order" class="doc-anchor">§</a>Order

The key-value pairs have a consistent order that is determined by the
sequence of insertion and removal calls on the map. The order does not
depend on the keys or the hash function at all.

All iterators traverse the map in *the order*.

The insertion order is preserved, with **notable exceptions** like the
`.remove()` or `.swap_remove()` methods. Methods such as `.sort_by()` of
course result in a new order, depending on the sorting order.

## <a href="#indices" class="doc-anchor">§</a>Indices

The key-value pairs are indexed in a compact range without holes in the
range `0..self.len()`. For example, the method `.get_full` looks up the
index for a key, and the method `.get_index` looks up the key-value pair
by index.

## <a href="#examples" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use indexmap::IndexMap;

// count the frequency of each letter in a sentence.
let mut letters = IndexMap::new();
for ch in "a short treatise on fungi".chars() {
    *letters.entry(ch).or_insert(0) += 1;
}

assert_eq!(letters[&'s'], 2);
assert_eq!(letters[&'t'], 3);
assert_eq!(letters[&'u'], 1);
assert_eq!(letters.get(&'y'), None);
```

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-IndexMap%3CK,+V%3E" class="section impl">

<a href="../../src/indexmap/map.rs.html#144-159"
class="src rightside">Source</a><a href="#impl-IndexMap%3CK,+V%3E" class="anchor">§</a>

### impl\<K, V\> <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V\>

</div>

<div class="impl-items">

<div id="method.new" class="section method">

<a href="../../src/indexmap/map.rs.html#147-149"
class="src rightside">Source</a>

#### pub fn <a href="#method.new" class="fn">new</a>() -\> Self

</div>

<div class="docblock">

Create a new map. (Does not allocate.)

</div>

<div id="method.with_capacity" class="section method">

<a href="../../src/indexmap/map.rs.html#156-158"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_capacity" class="fn">with_capacity</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> Self

</div>

<div class="docblock">

Create a new map with capacity for `n` key-value pairs. (Does not
allocate if `n` is zero.)

Computes in **O(n)** time.

</div>

</div>

<div id="impl-IndexMap%3CK,+V,+S%3E" class="section impl">

<a href="../../src/indexmap/map.rs.html#161-317"
class="src rightside">Source</a><a href="#impl-IndexMap%3CK,+V,+S%3E" class="anchor">§</a>

### impl\<K, V, S\> <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

</div>

<div class="impl-items">

<div id="method.with_capacity_and_hasher" class="section method">

<a href="../../src/indexmap/map.rs.html#167-176"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_capacity_and_hasher"
class="fn">with_capacity_and_hasher</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, hash_builder: S) -\> Self

</div>

<div class="docblock">

Create a new map with capacity for `n` key-value pairs. (Does not
allocate if `n` is zero.)

Computes in **O(n)** time.

</div>

<div id="method.with_hasher" class="section method">

<a href="../../src/indexmap/map.rs.html#182-187"
class="src rightside">Source</a>

#### pub const fn <a href="#method.with_hasher" class="fn">with_hasher</a>(hash_builder: S) -\> Self

</div>

<div class="docblock">

Create a new map with `hash_builder`.

This function is `const`, so it can be called in `static` contexts.

</div>

<div id="method.capacity" class="section method">

<a href="../../src/indexmap/map.rs.html#190-192"
class="src rightside">Source</a>

#### pub fn <a href="#method.capacity" class="fn">capacity</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Computes in **O(1)** time.

</div>

<div id="method.hasher" class="section method">

<a href="../../src/indexmap/map.rs.html#195-197"
class="src rightside">Source</a>

#### pub fn <a href="#method.hasher" class="fn">hasher</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;S</a>

</div>

<div class="docblock">

Return a reference to the map’s `BuildHasher`.

</div>

<div id="method.len" class="section method">

<a href="../../src/indexmap/map.rs.html#203-205"
class="src rightside">Source</a>

#### pub fn <a href="#method.len" class="fn">len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Return the number of key-value pairs in the map.

Computes in **O(1)** time.

</div>

<div id="method.is_empty" class="section method">

<a href="../../src/indexmap/map.rs.html#211-213"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_empty" class="fn">is_empty</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns true if the map contains no elements.

Computes in **O(1)** time.

</div>

<div id="method.iter" class="section method">

<a href="../../src/indexmap/map.rs.html#216-220"
class="src rightside">Source</a>

#### pub fn <a href="#method.iter" class="fn">iter</a>(&self) -\> <a href="struct.Iter.html" class="struct"
title="struct indexmap::map::Iter">Iter</a>\<'\_, K, V\> <a href="#" class="tooltip"
data-notable-ty="Iter&lt;&#39;_, K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

Return an iterator over the key-value pairs of the map, in their order

</div>

<div id="method.iter_mut" class="section method">

<a href="../../src/indexmap/map.rs.html#223-227"
class="src rightside">Source</a>

#### pub fn <a href="#method.iter_mut" class="fn">iter_mut</a>(&mut self) -\> <a href="struct.IterMut.html" class="struct"
title="struct indexmap::map::IterMut">IterMut</a>\<'\_, K, V\> <a href="#" class="tooltip"
data-notable-ty="IterMut&lt;&#39;_, K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

Return an iterator over the key-value pairs of the map, in their order

</div>

<div id="method.keys" class="section method">

<a href="../../src/indexmap/map.rs.html#230-234"
class="src rightside">Source</a>

#### pub fn <a href="#method.keys" class="fn">keys</a>(&self) -\> <a href="struct.Keys.html" class="struct"
title="struct indexmap::map::Keys">Keys</a>\<'\_, K, V\> <a href="#" class="tooltip"
data-notable-ty="Keys&lt;&#39;_, K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

Return an iterator over the keys of the map, in their order

</div>

<div id="method.into_keys" class="section method">

<a href="../../src/indexmap/map.rs.html#237-241"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_keys" class="fn">into_keys</a>(self) -\> <a href="struct.IntoKeys.html" class="struct"
title="struct indexmap::map::IntoKeys">IntoKeys</a>\<K, V\> <a href="#" class="tooltip" data-notable-ty="IntoKeys&lt;K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

Return an owning iterator over the keys of the map, in their order

</div>

<div id="method.values" class="section method">

<a href="../../src/indexmap/map.rs.html#244-248"
class="src rightside">Source</a>

#### pub fn <a href="#method.values" class="fn">values</a>(&self) -\> <a href="struct.Values.html" class="struct"
title="struct indexmap::map::Values">Values</a>\<'\_, K, V\> <a href="#" class="tooltip"
data-notable-ty="Values&lt;&#39;_, K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

Return an iterator over the values of the map, in their order

</div>

<div id="method.values_mut" class="section method">

<a href="../../src/indexmap/map.rs.html#252-256"
class="src rightside">Source</a>

#### pub fn <a href="#method.values_mut" class="fn">values_mut</a>(&mut self) -\> <a href="struct.ValuesMut.html" class="struct"
title="struct indexmap::map::ValuesMut">ValuesMut</a>\<'\_, K, V\> <a href="#" class="tooltip"
data-notable-ty="ValuesMut&lt;&#39;_, K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

Return an iterator over mutable references to the values of the map, in
their order

</div>

<div id="method.into_values" class="section method">

<a href="../../src/indexmap/map.rs.html#259-263"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_values" class="fn">into_values</a>(self) -\> <a href="struct.IntoValues.html" class="struct"
title="struct indexmap::map::IntoValues">IntoValues</a>\<K, V\> <a href="#" class="tooltip"
data-notable-ty="IntoValues&lt;K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

Return an owning iterator over the values of the map, in their order

</div>

<div id="method.clear" class="section method">

<a href="../../src/indexmap/map.rs.html#268-270"
class="src rightside">Source</a>

#### pub fn <a href="#method.clear" class="fn">clear</a>(&mut self)

</div>

<div class="docblock">

Remove all key-value pairs in the map, while preserving its capacity.

Computes in **O(n)** time.

</div>

<div id="method.truncate" class="section method">

<a href="../../src/indexmap/map.rs.html#275-277"
class="src rightside">Source</a>

#### pub fn <a href="#method.truncate" class="fn">truncate</a>(&mut self, len: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Shortens the map, keeping the first `len` elements and dropping the
rest.

If `len` is greater than the map’s current length, this has no effect.

</div>

<div id="method.drain" class="section method">

<a href="../../src/indexmap/map.rs.html#292-299"
class="src rightside">Source</a>

#### pub fn <a href="#method.drain" class="fn">drain</a>\<R\>(&mut self, range: R) -\> <a href="struct.Drain.html" class="struct"
title="struct indexmap::map::Drain">Drain</a>\<'\_, K, V\> <a href="#" class="tooltip"
data-notable-ty="Drain&lt;&#39;_, K, V&gt;">ⓘ</a>

<div class="where">

where R: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/range/trait.RangeBounds.html"
class="trait"
title="trait core::ops::range::RangeBounds">RangeBounds</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\>,

</div>

</div>

<div class="docblock">

Clears the `IndexMap` in the given index range, returning those
key-value pairs as a drain iterator.

The range may be any type that implements `RangeBounds<usize>`,
including all of the `std::ops::Range*` types, or even a tuple pair of
`Bound` start and end values. To drain the map entirely, use `RangeFull`
like `map.drain(..)`.

This shifts down all entries following the drained range to fill the
gap, and keeps the allocated memory for reuse.

***Panics*** if the starting point is greater than the end point or if
the end point is greater than the length of the map.

</div>

<div id="method.split_off" class="section method">

<a href="../../src/indexmap/map.rs.html#308-316"
class="src rightside">Source</a>

#### pub fn <a href="#method.split_off" class="fn">split_off</a>(&mut self, at: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> Self

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="docblock">

Splits the collection into two at the given index.

Returns a newly allocated map containing the elements in the range
`[at, len)`. After the call, the original map will be left containing
the elements `[0, at)` with its previous capacity unchanged.

***Panics*** if `at > len`.

</div>

</div>

<div id="impl-IndexMap%3CK,+V,+S%3E-1" class="section impl">

<a href="../../src/indexmap/map.rs.html#319-773"
class="src rightside">Source</a><a href="#impl-IndexMap%3CK,+V,+S%3E-1" class="anchor">§</a>

### impl\<K, V, S\> <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="impl-items">

<div id="method.reserve" class="section method">

<a href="../../src/indexmap/map.rs.html#327-329"
class="src rightside">Source</a>

#### pub fn <a href="#method.reserve" class="fn">reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Reserve capacity for `additional` more key-value pairs.

Computes in **O(n)** time.

</div>

<div id="method.shrink_to_fit" class="section method">

<a href="../../src/indexmap/map.rs.html#334-336"
class="src rightside">Source</a>

#### pub fn <a href="#method.shrink_to_fit" class="fn">shrink_to_fit</a>(&mut self)

</div>

<div class="docblock">

Shrink the capacity of the map as much as possible.

Computes in **O(n)** time.

</div>

<div id="method.shrink_to" class="section method">

<a href="../../src/indexmap/map.rs.html#341-343"
class="src rightside">Source</a>

#### pub fn <a href="#method.shrink_to" class="fn">shrink_to</a>(&mut self, min_capacity: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Shrink the capacity of the map with a lower limit.

Computes in **O(n)** time.

</div>

<div id="method.insert" class="section method">

<a href="../../src/indexmap/map.rs.html#364-366"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(&mut self, key: K, value: V) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<V\>

</div>

<div class="docblock">

Insert a key-value pair in the map.

If an equivalent key already exists in the map: the key remains and
retains in its place in the order, its corresponding value is updated
with `value` and the older value is returned inside `Some(_)`.

If no equivalent key existed in the map: the new key-value pair is
inserted, last in order, and `None` is returned.

Computes in **O(1)** time (amortized average).

See also [`entry`](#method.entry) if you you want to insert *or* modify
or if you need to get the index of the corresponding key-value pair.

</div>

<div id="method.insert_full" class="section method">

<a href="../../src/indexmap/map.rs.html#381-384"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert_full" class="fn">insert_full</a>(&mut self, key: K, value: V) -\> (<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<V\>)

</div>

<div class="docblock">

Insert a key-value pair in the map, and get their index.

If an equivalent key already exists in the map: the key remains and
retains in its place in the order, its corresponding value is updated
with `value` and the older value is returned inside `(index, Some(_))`.

If no equivalent key existed in the map: the new key-value pair is
inserted, last in order, and `(index, None)` is returned.

Computes in **O(1)** time (amortized average).

See also [`entry`](#method.entry) if you you want to insert *or* modify
or if you need to get the index of the corresponding key-value pair.

</div>

<div id="method.entry" class="section method">

<a href="../../src/indexmap/map.rs.html#390-393"
class="src rightside">Source</a>

#### pub fn <a href="#method.entry" class="fn">entry</a>(&mut self, key: K) -\> <a href="enum.Entry.html" class="enum"
title="enum indexmap::map::Entry">Entry</a>\<'\_, K, V\>

</div>

<div class="docblock">

Get the given key’s corresponding entry in the map for insertion and/or
in-place manipulation.

Computes in **O(1)** time (amortized average).

</div>

<div id="method.contains_key" class="section method">

<a href="../../src/indexmap/map.rs.html#398-403"
class="src rightside">Source</a>

#### pub fn <a href="#method.contains_key" class="fn">contains_key</a>\<Q\>(&self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Return `true` if an equivalent to `key` exists in the map.

Computes in **O(1)** time (average).

</div>

<div id="method.get" class="section method">

<a href="../../src/indexmap/map.rs.html#409-419"
class="src rightside">Source</a>

#### pub fn <a href="#method.get" class="fn">get</a>\<Q\>(&self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Return a reference to the value stored for `key`, if it is present, else
`None`.

Computes in **O(1)** time (average).

</div>

<div id="method.get_key_value" class="section method">

<a href="../../src/indexmap/map.rs.html#425-435"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_key_value" class="fn">get_key_value</a>\<Q\>(&self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>)\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Return references to the key-value pair stored for `key`, if it is
present, else `None`.

Computes in **O(1)** time (average).

</div>

<div id="method.get_full" class="section method">

<a href="../../src/indexmap/map.rs.html#438-448"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_full" class="fn">get_full</a>\<Q\>(&self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>)\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Return item index, key and value

</div>

<div id="method.get_index_of" class="section method">

<a href="../../src/indexmap/map.rs.html#453-463"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_index_of" class="fn">get_index_of</a>\<Q\>(&self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Return item index, if it exists in the map

Computes in **O(1)** time (average).

</div>

<div id="method.get_mut" class="section method">

<a href="../../src/indexmap/map.rs.html#465-475"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_mut" class="fn">get_mut</a>\<Q\>(&mut self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut V</a>\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div id="method.get_full_mut" class="section method">

<a href="../../src/indexmap/map.rs.html#477-487"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_full_mut" class="fn">get_full_mut</a>\<Q\>(&mut self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut V</a>)\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div id="method.remove" class="section method">

<a href="../../src/indexmap/map.rs.html#512-517"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove" class="fn">remove</a>\<Q\>(&mut self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<V\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Remove the key-value pair equivalent to `key` and return its value.

**NOTE:** This is equivalent to `.swap_remove(key)`, if you need to
preserve the order of the keys in the map, use `.shift_remove(key)`
instead.

Computes in **O(1)** time (average).

</div>

<div id="method.remove_entry" class="section method">

<a href="../../src/indexmap/map.rs.html#526-531"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove_entry" class="fn">remove_entry</a>\<Q\>(&mut self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Remove and return the key-value pair equivalent to `key`.

**NOTE:** This is equivalent to `.swap_remove_entry(key)`, if you need
to preserve the order of the keys in the map, use
`.shift_remove_entry(key)` instead.

Computes in **O(1)** time (average).

</div>

<div id="method.swap_remove" class="section method">

<a href="../../src/indexmap/map.rs.html#543-548"
class="src rightside">Source</a>

#### pub fn <a href="#method.swap_remove" class="fn">swap_remove</a>\<Q\>(&mut self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<V\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Remove the key-value pair equivalent to `key` and return its value.

Like `Vec::swap_remove`, the pair is removed by swapping it with the
last element of the map and popping it off. **This perturbs the position
of what used to be the last element!**

Return `None` if `key` is not in map.

Computes in **O(1)** time (average).

</div>

<div id="method.swap_remove_entry" class="section method">

<a href="../../src/indexmap/map.rs.html#559-567"
class="src rightside">Source</a>

#### pub fn <a href="#method.swap_remove_entry" class="fn">swap_remove_entry</a>\<Q\>(&mut self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Remove and return the key-value pair equivalent to `key`.

Like `Vec::swap_remove`, the pair is removed by swapping it with the
last element of the map and popping it off. **This perturbs the position
of what used to be the last element!**

Return `None` if `key` is not in map.

Computes in **O(1)** time (average).

</div>

<div id="method.swap_remove_full" class="section method">

<a href="../../src/indexmap/map.rs.html#579-588"
class="src rightside">Source</a>

#### pub fn <a href="#method.swap_remove_full" class="fn">swap_remove_full</a>\<Q\>(&mut self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, K, V)\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Remove the key-value pair equivalent to `key` and return it and the
index it had.

Like `Vec::swap_remove`, the pair is removed by swapping it with the
last element of the map and popping it off. **This perturbs the position
of what used to be the last element!**

Return `None` if `key` is not in map.

Computes in **O(1)** time (average).

</div>

<div id="method.shift_remove" class="section method">

<a href="../../src/indexmap/map.rs.html#600-605"
class="src rightside">Source</a>

#### pub fn <a href="#method.shift_remove" class="fn">shift_remove</a>\<Q\>(&mut self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<V\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Remove the key-value pair equivalent to `key` and return its value.

Like `Vec::remove`, the pair is removed by shifting all of the elements
that follow it, preserving their relative order. **This perturbs the
index of all of those elements!**

Return `None` if `key` is not in map.

Computes in **O(n)** time (average).

</div>

<div id="method.shift_remove_entry" class="section method">

<a href="../../src/indexmap/map.rs.html#616-624"
class="src rightside">Source</a>

#### pub fn <a href="#method.shift_remove_entry" class="fn">shift_remove_entry</a>\<Q\>(&mut self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Remove and return the key-value pair equivalent to `key`.

Like `Vec::remove`, the pair is removed by shifting all of the elements
that follow it, preserving their relative order. **This perturbs the
index of all of those elements!**

Return `None` if `key` is not in map.

Computes in **O(n)** time (average).

</div>

<div id="method.shift_remove_full" class="section method">

<a href="../../src/indexmap/map.rs.html#636-645"
class="src rightside">Source</a>

#### pub fn <a href="#method.shift_remove_full" class="fn">shift_remove_full</a>\<Q\>(&mut self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, K, V)\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Remove the key-value pair equivalent to `key` and return it and the
index it had.

Like `Vec::remove`, the pair is removed by shifting all of the elements
that follow it, preserving their relative order. **This perturbs the
index of all of those elements!**

Return `None` if `key` is not in map.

Computes in **O(n)** time (average).

</div>

<div id="method.pop" class="section method">

<a href="../../src/indexmap/map.rs.html#652-654"
class="src rightside">Source</a>

#### pub fn <a href="#method.pop" class="fn">pop</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>\>

</div>

<div class="docblock">

Remove the last key-value pair

This preserves the order of the remaining elements.

Computes in **O(1)** time (average).

</div>

<div id="method.retain" class="section method">

<a href="../../src/indexmap/map.rs.html#663-668"
class="src rightside">Source</a>

#### pub fn <a href="#method.retain" class="fn">retain</a>\<F\>(&mut self, keep: F)

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut V</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Scan through each key-value pair in the map and keep those where the
closure `keep` returns `true`.

The elements are visited in order, and remaining elements keep their
order.

Computes in **O(n)** time (average).

</div>

<div id="method.sort_keys" class="section method">

<a href="../../src/indexmap/map.rs.html#680-687"
class="src rightside">Source</a>

#### pub fn <a href="#method.sort_keys" class="fn">sort_keys</a>(&mut self)

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html"
class="trait" title="trait core::cmp::Ord">Ord</a>,

</div>

</div>

<div class="docblock">

Sort the map’s key-value pairs by the default ordering of the keys.

See
[`sort_by`](struct.IndexMap.html#method.sort_by "method indexmap::map::IndexMap::sort_by")
for details.

</div>

<div id="method.sort_by" class="section method">

<a href="../../src/indexmap/map.rs.html#697-704"
class="src rightside">Source</a>

#### pub fn <a href="#method.sort_by" class="fn">sort_by</a>\<F\>(&mut self, cmp: F)

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>,

</div>

</div>

<div class="docblock">

Sort the map’s key-value pairs in place using the comparison function
`cmp`.

The comparison function receives two key and value pairs to compare (you
can sort by keys or values or their combination as needed).

Computes in **O(n log n + c)** time and **O(n)** space where *n* is the
length of the map and *c* the capacity. The sort is stable.

</div>

<div id="method.sorted_by" class="section method">

<a href="../../src/indexmap/map.rs.html#710-719"
class="src rightside">Source</a>

#### pub fn <a href="#method.sorted_by" class="fn">sorted_by</a>\<F\>(self, cmp: F) -\> <a href="struct.IntoIter.html" class="struct"
title="struct indexmap::map::IntoIter">IntoIter</a>\<K, V\> <a href="#" class="tooltip" data-notable-ty="IntoIter&lt;K, V&gt;">ⓘ</a>

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>,

</div>

</div>

<div class="docblock">

Sort the key-value pairs of the map and return a by-value iterator of
the key-value pairs with the result.

The sort is stable.

</div>

<div id="method.sort_unstable_keys" class="section method">

<a href="../../src/indexmap/map.rs.html#725-732"
class="src rightside">Source</a>

#### pub fn <a href="#method.sort_unstable_keys" class="fn">sort_unstable_keys</a>(&mut self)

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html"
class="trait" title="trait core::cmp::Ord">Ord</a>,

</div>

</div>

<div class="docblock">

Sort the map’s key-value pairs by the default ordering of the keys, but
may not preserve the order of equal elements.

See
[`sort_unstable_by`](struct.IndexMap.html#method.sort_unstable_by "method indexmap::map::IndexMap::sort_unstable_by")
for details.

</div>

<div id="method.sort_unstable_by" class="section method">

<a href="../../src/indexmap/map.rs.html#742-749"
class="src rightside">Source</a>

#### pub fn <a href="#method.sort_unstable_by" class="fn">sort_unstable_by</a>\<F\>(&mut self, cmp: F)

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>,

</div>

</div>

<div class="docblock">

Sort the map’s key-value pairs in place using the comparison function
`cmp`, but may not preserve the order of equal elements.

The comparison function receives two key and value pairs to compare (you
can sort by keys or values or their combination as needed).

Computes in **O(n log n + c)** time where *n* is the length of the map
and *c* is the capacity. The sort is unstable.

</div>

<div id="method.sorted_unstable_by" class="section method">

<a href="../../src/indexmap/map.rs.html#756-765"
class="src rightside">Source</a>

#### pub fn <a href="#method.sorted_unstable_by" class="fn">sorted_unstable_by</a>\<F\>(self, cmp: F) -\> <a href="struct.IntoIter.html" class="struct"
title="struct indexmap::map::IntoIter">IntoIter</a>\<K, V\> <a href="#" class="tooltip" data-notable-ty="IntoIter&lt;K, V&gt;">ⓘ</a>

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>,

</div>

</div>

<div class="docblock">

Sort the key-value pairs of the map and return a by-value iterator of
the key-value pairs with the result.

The sort is unstable.

</div>

<div id="method.reverse" class="section method">

<a href="../../src/indexmap/map.rs.html#770-772"
class="src rightside">Source</a>

#### pub fn <a href="#method.reverse" class="fn">reverse</a>(&mut self)

</div>

<div class="docblock">

Reverses the order of the map’s key-value pairs in place.

Computes in **O(n)** time and **O(1)** space.

</div>

</div>

<div id="impl-IndexMap%3CK,+V,+S%3E-2" class="section impl">

<a href="../../src/indexmap/map.rs.html#775-867"
class="src rightside">Source</a><a href="#impl-IndexMap%3CK,+V,+S%3E-2" class="anchor">§</a>

### impl\<K, V, S\> <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

</div>

<div class="impl-items">

<div id="method.get_index" class="section method">

<a href="../../src/indexmap/map.rs.html#781-783"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_index" class="fn">get_index</a>(&self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>)\>

</div>

<div class="docblock">

Get a key-value pair by index

Valid indices are *0 \<= index \< self.len()*

Computes in **O(1)** time.

</div>

<div id="method.get_index_mut" class="section method">

<a href="../../src/indexmap/map.rs.html#790-792"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_index_mut" class="fn">get_index_mut</a>(&mut self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut V</a>)\>

</div>

<div class="docblock">

Get a key-value pair by index

Valid indices are *0 \<= index \< self.len()*

Computes in **O(1)** time.

</div>

<div id="method.first" class="section method">

<a href="../../src/indexmap/map.rs.html#797-799"
class="src rightside">Source</a>

#### pub fn <a href="#method.first" class="fn">first</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>)\>

</div>

<div class="docblock">

Get the first key-value pair

Computes in **O(1)** time.

</div>

<div id="method.first_mut" class="section method">

<a href="../../src/indexmap/map.rs.html#804-806"
class="src rightside">Source</a>

#### pub fn <a href="#method.first_mut" class="fn">first_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut V</a>)\>

</div>

<div class="docblock">

Get the first key-value pair, with mutable access to the value

Computes in **O(1)** time.

</div>

<div id="method.last" class="section method">

<a href="../../src/indexmap/map.rs.html#811-813"
class="src rightside">Source</a>

#### pub fn <a href="#method.last" class="fn">last</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>)\>

</div>

<div class="docblock">

Get the last key-value pair

Computes in **O(1)** time.

</div>

<div id="method.last_mut" class="section method">

<a href="../../src/indexmap/map.rs.html#818-820"
class="src rightside">Source</a>

#### pub fn <a href="#method.last_mut" class="fn">last_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut V</a>)\>

</div>

<div class="docblock">

Get the last key-value pair, with mutable access to the value

Computes in **O(1)** time.

</div>

<div id="method.swap_remove_index" class="section method">

<a href="../../src/indexmap/map.rs.html#831-833"
class="src rightside">Source</a>

#### pub fn <a href="#method.swap_remove_index" class="fn">swap_remove_index</a>(&mut self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>\>

</div>

<div class="docblock">

Remove the key-value pair by index

Valid indices are *0 \<= index \< self.len()*

Like `Vec::swap_remove`, the pair is removed by swapping it with the
last element of the map and popping it off. **This perturbs the position
of what used to be the last element!**

Computes in **O(1)** time (average).

</div>

<div id="method.shift_remove_index" class="section method">

<a href="../../src/indexmap/map.rs.html#844-846"
class="src rightside">Source</a>

#### pub fn <a href="#method.shift_remove_index" class="fn">shift_remove_index</a>(&mut self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>\>

</div>

<div class="docblock">

Remove the key-value pair by index

Valid indices are *0 \<= index \< self.len()*

Like `Vec::remove`, the pair is removed by shifting all of the elements
that follow it, preserving their relative order. **This perturbs the
index of all of those elements!**

Computes in **O(n)** time (average).

</div>

<div id="method.move_index" class="section method">

<a href="../../src/indexmap/map.rs.html#857-859"
class="src rightside">Source</a>

#### pub fn <a href="#method.move_index" class="fn">move_index</a>(&mut self, from: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, to: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Moves the position of a key-value pair from one index to another by
shifting all other pairs in-between.

- If `from < to`, the other pairs will shift down while the targeted
  pair moves up.
- If `from > to`, the other pairs will shift up while the targeted pair
  moves down.

***Panics*** if `from` or `to` are out of bounds.

Computes in **O(n)** time (average).

</div>

<div id="method.swap_indices" class="section method">

<a href="../../src/indexmap/map.rs.html#864-866"
class="src rightside">Source</a>

#### pub fn <a href="#method.swap_indices" class="fn">swap_indices</a>(&mut self, a: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, b: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Swaps the position of two key-value pairs in the map.

***Panics*** if `a` or `b` are out of bounds.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-IndexMap%3CK,+V,+S%3E" class="section impl">

<a href="../../src/indexmap/map.rs.html#81-98"
class="src rightside">Source</a><a href="#impl-Clone-for-IndexMap%3CK,+V,+S%3E" class="anchor">§</a>

### impl\<K, V, S\> <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, S:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#87-92"
class="src rightside">Source</a><a href="#method.clone" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone"
class="fn">clone</a>(&self) -\> Self

</div>

<div class="docblock">

Returns a duplicate of the value. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone)

</div>

<div id="method.clone_from" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#94-97"
class="src rightside">Source</a><a href="#method.clone_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from"
class="fn">clone_from</a>(&mut self, other: &Self)

</div>

<div class="docblock">

Performs copy-assignment from `source`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from)

</div>

</div>

<div id="impl-Debug-for-IndexMap%3CK,+V,+S%3E" class="section impl">

<a href="../../src/indexmap/map.rs.html#126-141"
class="src rightside">Source</a><a href="#impl-Debug-for-IndexMap%3CK,+V,+S%3E" class="anchor">§</a>

### impl\<K, V, S\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>,

</div>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#131-140"
class="src rightside">Source</a><a href="#method.fmt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt"
class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt)

</div>

</div>

<div id="impl-Default-for-IndexMap%3CK,+V,+S%3E" class="section impl">

<a href="../../src/indexmap/map.rs.html#1490-1498"
class="src rightside">Source</a><a href="#impl-Default-for-IndexMap%3CK,+V,+S%3E" class="anchor">§</a>

### impl\<K, V, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where S: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>,

</div>

</div>

<div class="impl-items">

<div id="method.default" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#1495-1497"
class="src rightside">Source</a><a href="#method.default" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html#tymethod.default"
class="fn">default</a>() -\> Self

</div>

<div class="docblock">

Return an empty `IndexMap`

</div>

</div>

<div id="impl-Extend%3C(%26K,+%26V)%3E-for-IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="../../src/indexmap/map.rs.html#1476-1488"
class="src rightside">Source</a><a href="#impl-Extend%3C(%26K,+%26V)%3E-for-IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<'a, K, V, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a V</a>)\> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="impl-items">

<div id="method.extend-1" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#1485-1487"
class="src rightside">Source</a><a href="#method.extend-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = (<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a V</a>)\>\>(&mut self, iterable: I)

</div>

<div class="docblock">

Extend the map with all key-value pairs in the iterable.

See the first extend method for more details.

</div>

<div id="method.extend_one-1" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#417"
class="src rightside">Source</a><a href="#method.extend_one-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_one"
class="fn">extend_one</a>(&mut self, item: A)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`extend_one`)

</div>

<div class="docblock">

Extends a collection with exactly one element.

</div>

<div id="method.extend_reserve-1" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#425"
class="src rightside">Source</a><a href="#method.extend_reserve-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_reserve"
class="fn">extend_reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`extend_one`)

</div>

<div class="docblock">

Reserves capacity in a collection for the given number of additional
elements. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_reserve)

</div>

</div>

<div id="impl-Extend%3C(K,+V)%3E-for-IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="../../src/indexmap/map.rs.html#1443-1474"
class="src rightside">Source</a><a href="#impl-Extend%3C(K,+V)%3E-for-IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<K, V, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>\> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="impl-items">

<div id="method.extend" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#1457-1473"
class="src rightside">Source</a><a href="#method.extend" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>\>\>(&mut self, iterable: I)

</div>

<div class="docblock">

Extend the map with all key-value pairs in the iterable.

This is equivalent to calling [`insert`](#method.insert) for each of
them in order, which means that for keys that already existed in the
map, their value is updated but it keeps the existing order.

New keys are inserted in the order they appear in the sequence. If
equivalents of a key occur more than once, the last corresponding value
prevails.

</div>

<div id="method.extend_one" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#417"
class="src rightside">Source</a><a href="#method.extend_one" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_one"
class="fn">extend_one</a>(&mut self, item: A)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`extend_one`)

</div>

<div class="docblock">

Extends a collection with exactly one element.

</div>

<div id="method.extend_reserve" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#425"
class="src rightside">Source</a><a href="#method.extend_reserve" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_reserve"
class="fn">extend_reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`extend_one`)

</div>

<div class="docblock">

Reserves capacity in a collection for the given number of additional
elements. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_reserve)

</div>

</div>

<div id="impl-From%3C%5B(K,+V);+N%5D%3E-for-IndexMap%3CK,+V%3E"
class="section impl">

<a href="../../src/indexmap/map.rs.html#1425-1441"
class="src rightside">Source</a><a href="#impl-From%3C%5B(K,+V);+N%5D%3E-for-IndexMap%3CK,+V%3E"
class="anchor">§</a>

### impl\<K, V, const N: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<\[<a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>; <a href="https://doc.rust-lang.org/1.92.0/std/primitive.array.html"
class="primitive">N</a>\]\> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, <a
href="https://doc.rust-lang.org/1.92.0/std/hash/random/struct.RandomState.html"
class="struct"
title="struct std::hash::random::RandomState">RandomState</a>\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a>,

</div>

<span class="item-info"></span>

<div class="stab portability">

Available on **`has_std`** only.

</div>

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#1438-1440"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(arr: \[<a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>; <a href="https://doc.rust-lang.org/1.92.0/std/primitive.array.html"
class="primitive">N</a>\]) -\> Self

</div>

<div class="docblock">

##### <a href="#examples-5" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use indexmap::IndexMap;

let map1 = IndexMap::from([(1, 2), (3, 4)]);
let map2: IndexMap<_, _> = [(1, 2), (3, 4)].into();
assert_eq!(map1, map2);
```

</div>

</div>

</div>

<div id="impl-FromIterator%3C(K,+V)%3E-for-IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="../../src/indexmap/map.rs.html#1405-1422"
class="src rightside">Source</a><a href="#impl-FromIterator%3C(K,+V)%3E-for-IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<K, V, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html"
class="trait"
title="trait core::iter::traits::collect::FromIterator">FromIterator</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>\> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>,

</div>

</div>

<div class="impl-items">

<div id="method.from_iter" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#1415-1421"
class="src rightside">Source</a><a href="#method.from_iter" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html#tymethod.from_iter"
class="fn">from_iter</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>\>\>(iterable: I) -\> Self

</div>

<div class="docblock">

Create an `IndexMap` from the sequence of key-value pairs in the
iterable.

`from_iter` uses the same logic as `extend`. See
[`extend`](#method.extend) for more details.

</div>

</div>

<div id="impl-Index%3C%26Q%3E-for-IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="../../src/indexmap/map.rs.html#1265-1279"
class="src rightside">Source</a><a href="#impl-Index%3C%26Q%3E-for-IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<K, V, Q, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html"
class="trait" title="trait core::ops::index::Index">Index</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>\> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

<div class="docblock">

Access `IndexMap` values corresponding to a key.

</div>

</div>

<div class="docblock">

#### <a href="#examples-1" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use indexmap::IndexMap;

let mut map = IndexMap::new();
for word in "Lorem ipsum dolor sit amet".split_whitespace() {
    map.insert(word.to_lowercase(), word.to_uppercase());
}
assert_eq!(map["lorem"], "LOREM");
assert_eq!(map["ipsum"], "IPSUM");
```

</div>

<div class="example-wrap should_panic">

<a href="#" class="tooltip" title="This example panics">ⓘ</a>

``` rust
use indexmap::IndexMap;

let mut map = IndexMap::new();
map.insert("foo", 1);
println!("{:?}", map["bar"]); // panics!
```

</div>

</div>

<div class="impl-items">

<div id="method.index" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#1276-1278"
class="src rightside">Source</a><a href="#method.index" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html#tymethod.index"
class="fn">index</a>(&self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>

</div>

<div class="docblock">

Returns a reference to the value corresponding to the supplied `key`.

***Panics*** if `key` is not present in the map.

</div>

<div id="associatedtype.Output"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/map.rs.html#1271"
class="src rightside">Source</a><a href="#associatedtype.Output" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html#associatedtype.Output"
class="associatedtype">Output</a> = V

</div>

<div class="docblock">

The returned type after indexing.

</div>

</div>

<div id="impl-Index%3Cusize%3E-for-IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="../../src/indexmap/map.rs.html#1352-1363"
class="src rightside">Source</a><a href="#impl-Index%3Cusize%3E-for-IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<K, V, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html"
class="trait" title="trait core::ops::index::Index">Index</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="docblock">

Access `IndexMap` values at indexed positions.

</div>

</div>

<div class="docblock">

#### <a href="#examples-3" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use indexmap::IndexMap;

let mut map = IndexMap::new();
for word in "Lorem ipsum dolor sit amet".split_whitespace() {
    map.insert(word.to_lowercase(), word.to_uppercase());
}
assert_eq!(map[0], "LOREM");
assert_eq!(map[1], "IPSUM");
map.reverse();
assert_eq!(map[0], "AMET");
assert_eq!(map[1], "SIT");
map.sort_keys();
assert_eq!(map[0], "AMET");
assert_eq!(map[1], "DOLOR");
```

</div>

<div class="example-wrap should_panic">

<a href="#" class="tooltip" title="This example panics">ⓘ</a>

``` rust
use indexmap::IndexMap;

let mut map = IndexMap::new();
map.insert("foo", 1);
println!("{:?}", map[10]); // panics!
```

</div>

</div>

<div class="impl-items">

<div id="method.index-1" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#1358-1362"
class="src rightside">Source</a><a href="#method.index-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html#tymethod.index"
class="fn">index</a>(&self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;V</a>

</div>

<div class="docblock">

Returns a reference to the value at the supplied `index`.

***Panics*** if `index` is out of bounds.

</div>

<div id="associatedtype.Output-1"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/map.rs.html#1353"
class="src rightside">Source</a><a href="#associatedtype.Output-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html#associatedtype.Output"
class="associatedtype">Output</a> = V

</div>

<div class="docblock">

The returned type after indexing.

</div>

</div>

<div id="impl-IndexMut%3C%26Q%3E-for-IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="../../src/indexmap/map.rs.html#1310-1322"
class="src rightside">Source</a><a href="#impl-IndexMut%3C%26Q%3E-for-IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<K, V, Q, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.IndexMut.html"
class="trait" title="trait core::ops::index::IndexMut">IndexMut</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>\> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

<div class="docblock">

Access `IndexMap` values corresponding to a key.

</div>

</div>

<div class="docblock">

Mutable indexing allows changing / updating values of key-value pairs
that are already present.

You can **not** insert new pairs with index syntax, use `.insert()`.

#### <a href="#examples-2" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use indexmap::IndexMap;

let mut map = IndexMap::new();
for word in "Lorem ipsum dolor sit amet".split_whitespace() {
    map.insert(word.to_lowercase(), word.to_string());
}
let lorem = &mut map["lorem"];
assert_eq!(lorem, "Lorem");
lorem.retain(char::is_lowercase);
assert_eq!(map["lorem"], "orem");
```

</div>

<div class="example-wrap should_panic">

<a href="#" class="tooltip" title="This example panics">ⓘ</a>

``` rust
use indexmap::IndexMap;

let mut map = IndexMap::new();
map.insert("foo", 1);
map["bar"] = 1; // panics!
```

</div>

</div>

<div class="impl-items">

<div id="method.index_mut" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#1319-1321"
class="src rightside">Source</a><a href="#method.index_mut" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.IndexMut.html#tymethod.index_mut"
class="fn">index_mut</a>(&mut self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut V</a>

</div>

<div class="docblock">

Returns a mutable reference to the value corresponding to the supplied
`key`.

***Panics*** if `key` is not present in the map.

</div>

</div>

<div id="impl-IndexMut%3Cusize%3E-for-IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="../../src/indexmap/map.rs.html#1394-1403"
class="src rightside">Source</a><a href="#impl-IndexMut%3Cusize%3E-for-IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<K, V, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.IndexMut.html"
class="trait" title="trait core::ops::index::IndexMut">IndexMut</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="docblock">

Access `IndexMap` values at indexed positions.

</div>

</div>

<div class="docblock">

Mutable indexing allows changing / updating indexed values that are
already present.

You can **not** insert new values with index syntax, use `.insert()`.

#### <a href="#examples-4" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use indexmap::IndexMap;

let mut map = IndexMap::new();
for word in "Lorem ipsum dolor sit amet".split_whitespace() {
    map.insert(word.to_lowercase(), word.to_string());
}
let lorem = &mut map[0];
assert_eq!(lorem, "Lorem");
lorem.retain(char::is_lowercase);
assert_eq!(map["lorem"], "orem");
```

</div>

<div class="example-wrap should_panic">

<a href="#" class="tooltip" title="This example panics">ⓘ</a>

``` rust
use indexmap::IndexMap;

let mut map = IndexMap::new();
map.insert("foo", 1);
map[10] = 1; // panics!
```

</div>

</div>

<div class="impl-items">

<div id="method.index_mut-1" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#1398-1402"
class="src rightside">Source</a><a href="#method.index_mut-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.IndexMut.html#tymethod.index_mut"
class="fn">index_mut</a>(&mut self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut V</a>

</div>

<div class="docblock">

Returns a mutable reference to the value at the supplied `index`.

***Panics*** if `index` is out of bounds.

</div>

</div>

<div id="impl-IntoIterator-for-%26IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="../../src/indexmap/map.rs.html#1217-1223"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-%26IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<'a, K, V, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for &'a <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

</div>

<div class="impl-items">

<div id="associatedtype.Item" class="section associatedtype trait-impl">

<a href="../../src/indexmap/map.rs.html#1218"
class="src rightside">Source</a><a href="#associatedtype.Item" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = (<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a V</a>)

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/map.rs.html#1219"
class="src rightside">Source</a><a href="#associatedtype.IntoIter" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="struct.Iter.html" class="struct"
title="struct indexmap::map::Iter">Iter</a>\<'a, K, V\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

<div id="method.into_iter" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#1220-1222"
class="src rightside">Source</a><a href="#method.into_iter" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter"
class="fn">into_iter</a>(self) -\> Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::IntoIter">IntoIter</a>

</div>

<div class="docblock">

Creates an iterator from a value. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter)

</div>

</div>

<div id="impl-IntoIterator-for-%26mut+IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="../../src/indexmap/map.rs.html#1225-1231"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-%26mut+IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<'a, K, V, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for &'a mut <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

</div>

<div class="impl-items">

<div id="associatedtype.Item-1"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/map.rs.html#1226"
class="src rightside">Source</a><a href="#associatedtype.Item-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = (<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a mut V</a>)

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter-1"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/map.rs.html#1227"
class="src rightside">Source</a><a href="#associatedtype.IntoIter-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="struct.IterMut.html" class="struct"
title="struct indexmap::map::IterMut">IterMut</a>\<'a, K, V\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

<div id="method.into_iter-1" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#1228-1230"
class="src rightside">Source</a><a href="#method.into_iter-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter"
class="fn">into_iter</a>(self) -\> Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::IntoIter">IntoIter</a>

</div>

<div class="docblock">

Creates an iterator from a value. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter)

</div>

</div>

<div id="impl-IntoIterator-for-IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="../../src/indexmap/map.rs.html#1233-1241"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<K, V, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

</div>

<div class="impl-items">

<div id="associatedtype.Item-2"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/map.rs.html#1234"
class="src rightside">Source</a><a href="#associatedtype.Item-2" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(K, V)</a>

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter-2"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/map.rs.html#1235"
class="src rightside">Source</a><a href="#associatedtype.IntoIter-2" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="struct.IntoIter.html" class="struct"
title="struct indexmap::map::IntoIter">IntoIter</a>\<K, V\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

<div id="method.into_iter-2" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#1236-1240"
class="src rightside">Source</a><a href="#method.into_iter-2" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter"
class="fn">into_iter</a>(self) -\> Self::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::IntoIter">IntoIter</a>

</div>

<div class="docblock">

Creates an iterator from a value. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter)

</div>

</div>

<div id="impl-MutableKeys-for-IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="../../src/indexmap/mutable_keys.rs.html#51-75"
class="src rightside">Source</a><a href="#impl-MutableKeys-for-IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<K, V, S\> <a href="trait.MutableKeys.html" class="trait"
title="trait indexmap::map::MutableKeys">MutableKeys</a> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

<div class="docblock">

Opt-in mutable access to keys.

</div>

</div>

<div class="docblock">

See [`MutableKeys`](trait.MutableKeys.html) for more information.

</div>

<div class="impl-items">

<div id="associatedtype.Key" class="section associatedtype trait-impl">

<a href="../../src/indexmap/mutable_keys.rs.html#56"
class="src rightside">Source</a><a href="#associatedtype.Key" class="anchor">§</a>

#### type <a href="trait.MutableKeys.html#associatedtype.Key"
class="associatedtype">Key</a> = K

</div>

<div id="associatedtype.Value"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/mutable_keys.rs.html#57"
class="src rightside">Source</a><a href="#associatedtype.Value" class="anchor">§</a>

#### type <a href="trait.MutableKeys.html#associatedtype.Value"
class="associatedtype">Value</a> = V

</div>

<div id="method.get_full_mut2" class="section method trait-impl">

<a href="../../src/indexmap/mutable_keys.rs.html#58-63"
class="src rightside">Source</a><a href="#method.get_full_mut2" class="anchor">§</a>

#### fn <a href="trait.MutableKeys.html#tymethod.get_full_mut2"
class="fn">get_full_mut2</a>\<Q\>(&mut self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut K</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut V</a>)\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Return item index, mutable reference to key and value

</div>

<div id="method.retain2" class="section method trait-impl">

<a href="../../src/indexmap/mutable_keys.rs.html#65-70"
class="src rightside">Source</a><a href="#method.retain2" class="anchor">§</a>

#### fn <a href="trait.MutableKeys.html#tymethod.retain2" class="fn">retain2</a>\<F\>(&mut self, keep: F)

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut K</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut V</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Scan through each key-value pair in the map and keep those where the
closure `keep` returns `true`. [Read
more](trait.MutableKeys.html#tymethod.retain2)

</div>

<div id="method.__private_marker" class="section method trait-impl">

<a href="../../src/indexmap/mutable_keys.rs.html#72-74"
class="src rightside">Source</a><a href="#method.__private_marker" class="anchor">§</a>

#### fn <a href="trait.MutableKeys.html#tymethod.__private_marker"
class="fn">__private_marker</a>(&self) -\> PrivateMarker

</div>

<div class="docblock">

This method is not useful in itself – it is there to “seal” the trait
for external implementation, so that we can add methods without causing
breaking changes.

</div>

</div>

<div id="impl-PartialEq%3CIndexMap%3CK,+V2,+S2%3E%3E-for-IndexMap%3CK,+V1,+S1%3E"
class="section impl">

<a href="../../src/indexmap/map.rs.html#1500-1515"
class="src rightside">Source</a><a
href="#impl-PartialEq%3CIndexMap%3CK,+V2,+S2%3E%3E-for-IndexMap%3CK,+V1,+S1%3E"
class="anchor">§</a>

### impl\<K, V1, S1, V2, S2\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a>\<<a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V2, S2\>\> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V1, S1\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a>, V1:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a>\<V2\>,
S1: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>, S2:
<a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../../src/indexmap/map.rs.html#1507-1514"
class="src rightside">Source</a><a href="#method.eq" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#tymethod.eq"
class="fn">eq</a>(&self, other: &<a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V2, S2\>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `self` and `other` values to be equal, and is used by `==`.

</div>

<div id="method.ne" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#264"
class="src">Source</a></span><a href="#method.ne" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#method.ne"
class="fn">ne</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `!=`. The default implementation is almost always sufficient,
and should not be overridden without very good reason.

</div>

</div>

<div id="impl-Eq-for-IndexMap%3CK,+V,+S%3E" class="section impl">

<a href="../../src/indexmap/map.rs.html#1517-1523"
class="src rightside">Source</a><a href="#impl-Eq-for-IndexMap%3CK,+V,+S%3E" class="anchor">§</a>

### impl\<K, V, S\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-IndexMap%3CK,+V,+S%3E" class="section impl">

<a href="#impl-Freeze-for-IndexMap%3CK,+V,+S%3E" class="anchor">§</a>

### impl\<K, V, S\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>,

</div>

</div>

<div id="impl-RefUnwindSafe-for-IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<K, V, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where S: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
K: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
V: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

<div id="impl-Send-for-IndexMap%3CK,+V,+S%3E" class="section impl">

<a href="#impl-Send-for-IndexMap%3CK,+V,+S%3E" class="anchor">§</a>

### impl\<K, V, S\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-IndexMap%3CK,+V,+S%3E" class="section impl">

<a href="#impl-Sync-for-IndexMap%3CK,+V,+S%3E" class="anchor">§</a>

### impl\<K, V, S\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>,

</div>

</div>

<div id="impl-Unpin-for-IndexMap%3CK,+V,+S%3E" class="section impl">

<a href="#impl-Unpin-for-IndexMap%3CK,+V,+S%3E" class="anchor">§</a>

### impl\<K, V, S\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-IndexMap%3CK,+V,+S%3E"
class="section impl">

<a href="#impl-UnwindSafe-for-IndexMap%3CK,+V,+S%3E"
class="anchor">§</a>

### impl\<K, V, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.IndexMap.html" class="struct"
title="struct indexmap::map::IndexMap">IndexMap</a>\<K, V, S\>

<div class="where">

where S: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a>, K: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a>, V: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a>,

</div>

</div>

</div>

## Blanket Implementations<a href="#blanket-implementations" class="anchor">§</a>

<div id="blanket-implementations-list">

<div id="impl-Any-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#138"
class="src rightside">Source</a><a href="#impl-Any-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html"
class="trait" title="trait core::any::Any">Any</a> for T

<div class="where">

where T: 'static +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.type_id" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#139"
class="src rightside">Source</a><a href="#method.type_id" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id"
class="fn">type_id</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/any/struct.TypeId.html"
class="struct" title="struct core::any::TypeId">TypeId</a>

</div>

<div class="docblock">

Gets the `TypeId` of `self`. [Read
more](https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id)

</div>

</div>

<div id="impl-Borrow%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#212"
class="src rightside">Source</a><a href="#impl-Borrow%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#214"
class="src rightside">Source</a><a href="#method.borrow" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow"
class="fn">borrow</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="docblock">

Immutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow)

</div>

</div>

<div id="impl-BorrowMut%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#221"
class="src rightside">Source</a><a href="#impl-BorrowMut%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html"
class="trait" title="trait core::borrow::BorrowMut">BorrowMut</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow_mut" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#222"
class="src rightside">Source</a><a href="#method.borrow_mut" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut"
class="fn">borrow_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>

</div>

<div class="docblock">

Mutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut)

</div>

</div>

<div id="impl-CloneToUninit-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#515"
class="src rightside">Source</a><a href="#impl-CloneToUninit-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html"
class="trait" title="trait core::clone::CloneToUninit">CloneToUninit</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.clone_to_uninit" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#517"
class="src rightside">Source</a><a href="#method.clone_to_uninit" class="anchor">§</a>

#### unsafe fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit"
class="fn">clone_to_uninit</a>(&self, dest: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.pointer.html"
class="primitive">*mut</a> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`clone_to_uninit`)

</div>

<div class="docblock">

Performs copy-assignment from `self` to `dest`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)

</div>

</div>

<div id="impl-Equivalent%3CK%3E-for-Q" class="section impl">

<a href="../../src/indexmap/equivalent.rs.html#18-27"
class="src rightside">Source</a><a href="#impl-Equivalent%3CK%3E-for-Q" class="anchor">§</a>

### impl\<Q, K\> <a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> for Q

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.equivalent" class="section method trait-impl">

<a href="../../src/indexmap/equivalent.rs.html#24-26"
class="src rightside">Source</a><a href="#method.equivalent" class="anchor">§</a>

#### fn <a href="../trait.Equivalent.html#tymethod.equivalent"
class="fn">equivalent</a>(&self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Compare self to `key` and return `true` if they are equal.

</div>

</div>

<div id="impl-From%3CT%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#785"
class="src rightside">Source</a><a href="#impl-From%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\> for T

</div>

<div class="impl-items">

<div id="method.from-1" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(t: T) -\> T

</div>

<div class="docblock">

Returns the argument unchanged.

</div>

</div>

<div id="impl-Into%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#767-769"
class="src rightside">Source</a><a href="#impl-Into%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="method.into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#777"
class="src rightside">Source</a><a href="#method.into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html#tymethod.into"
class="fn">into</a>(self) -\> U

</div>

<div class="docblock">

Calls `U::from(self)`.

That is, this conversion is whatever the implementation of
[`From`](https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html "trait core::convert::From")`<T> for U`
chooses to do.

</div>

</div>

<div id="impl-ToOwned-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#85-87"
class="src rightside">Source</a><a href="#impl-ToOwned-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html"
class="trait" title="trait alloc::borrow::ToOwned">ToOwned</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Owned"
class="section associatedtype trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#89"
class="src rightside">Source</a><a href="#associatedtype.Owned" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#associatedtype.Owned"
class="associatedtype">Owned</a> = T

</div>

<div class="docblock">

The resulting type after obtaining ownership.

</div>

<div id="method.to_owned" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#90"
class="src rightside">Source</a><a href="#method.to_owned" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned"
class="fn">to_owned</a>(&self) -\> T

</div>

<div class="docblock">

Creates owned data from borrowed data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned)

</div>

<div id="method.clone_into" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#94"
class="src rightside">Source</a><a href="#method.clone_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into"
class="fn">clone_into</a>(&self, target: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>)

</div>

<div class="docblock">

Uses borrowed data to replace owned data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into)

</div>

</div>

<div id="impl-TryFrom%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#827-829"
class="src rightside">Source</a><a href="#impl-TryFrom%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error-1"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#831"
class="src rightside">Source</a><a href="#associatedtype.Error-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype">Error</a> = <a
href="https://doc.rust-lang.org/1.92.0/core/convert/enum.Infallible.html"
class="enum" title="enum core::convert::Infallible">Infallible</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#834"
class="src rightside">Source</a><a href="#method.try_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#tymethod.try_from"
class="fn">try_from</a>(value: U) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<T, \<T as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

<div id="impl-TryInto%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#811-813"
class="src rightside">Source</a><a href="#impl-TryInto%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html"
class="trait" title="trait core::convert::TryInto">TryInto</a>\<U\> for T

<div class="where">

where U: <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#815"
class="src rightside">Source</a><a href="#associatedtype.Error" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#associatedtype.Error"
class="associatedtype">Error</a> = \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#818"
class="src rightside">Source</a><a href="#method.try_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#tymethod.try_into"
class="fn">try_into</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<U, \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

</div>

</div>

</div>
