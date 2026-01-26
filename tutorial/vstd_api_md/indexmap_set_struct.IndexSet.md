<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[indexmap](../index.html)::[set](index.html)

</div>

# Struct <span class="struct">IndexSet</span> Copy item path

<span class="sub-heading"><a href="../../src/indexmap/set.rs.html#63-65" class="src">Source</a>
</span>

</div>

``` rust
pub struct IndexSet<T, S = RandomState> { /* private fields */ }
```

Expand description

<div class="docblock">

A hash set where the iteration order of the values is independent of
their hash values.

The interface is closely compatible with the standard `HashSet`, but
also has additional features.

## <a href="#order" class="doc-anchor">§</a>Order

The values have a consistent order that is determined by the sequence of
insertion and removal calls on the set. The order does not depend on the
values or the hash function at all. Note that insertion order and value
are not affected if a re-insertion is attempted once an element is
already present.

All iterators traverse the set *in order*. Set operation iterators like
`union` produce a concatenated order, as do their matching “bitwise”
operators. See their documentation for specifics.

The insertion order is preserved, with **notable exceptions** like the
`.remove()` or `.swap_remove()` methods. Methods such as `.sort_by()` of
course result in a new order, depending on the sorting order.

## <a href="#indices" class="doc-anchor">§</a>Indices

The values are indexed in a compact range without holes in the range
`0..self.len()`. For example, the method `.get_full` looks up the index
for a value, and the method `.get_index` looks up the value by index.

## <a href="#examples" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use indexmap::IndexSet;

// Collects which letters appear in a sentence.
let letters: IndexSet<_> = "a short treatise on fungi".chars().collect();

assert!(letters.contains(&'s'));
assert!(letters.contains(&'t'));
assert!(letters.contains(&'u'));
assert!(!letters.contains(&'y'));
```

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-IndexSet%3CT%3E" class="section impl">

<a href="../../src/indexmap/set.rs.html#128-145"
class="src rightside">Source</a><a href="#impl-IndexSet%3CT%3E" class="anchor">§</a>

### impl\<T\> <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T\>

</div>

<div class="impl-items">

<div id="method.new" class="section method">

<a href="../../src/indexmap/set.rs.html#130-134"
class="src rightside">Source</a>

#### pub fn <a href="#method.new" class="fn">new</a>() -\> Self

</div>

<div class="docblock">

Create a new set. (Does not allocate.)

</div>

<div id="method.with_capacity" class="section method">

<a href="../../src/indexmap/set.rs.html#140-144"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_capacity" class="fn">with_capacity</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> Self

</div>

<div class="docblock">

Create a new set with capacity for `n` elements. (Does not allocate if
`n` is zero.)

Computes in **O(n)** time.

</div>

</div>

<div id="impl-IndexSet%3CT,+S%3E" class="section impl">

<a href="../../src/indexmap/set.rs.html#147-250"
class="src rightside">Source</a><a href="#impl-IndexSet%3CT,+S%3E" class="anchor">§</a>

### impl\<T, S\> <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

</div>

<div class="impl-items">

<div id="method.with_capacity_and_hasher" class="section method">

<a href="../../src/indexmap/set.rs.html#152-156"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_capacity_and_hasher"
class="fn">with_capacity_and_hasher</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, hash_builder: S) -\> Self

</div>

<div class="docblock">

Create a new set with capacity for `n` elements. (Does not allocate if
`n` is zero.)

Computes in **O(n)** time.

</div>

<div id="method.with_hasher" class="section method">

<a href="../../src/indexmap/set.rs.html#162-166"
class="src rightside">Source</a>

#### pub const fn <a href="#method.with_hasher" class="fn">with_hasher</a>(hash_builder: S) -\> Self

</div>

<div class="docblock">

Create a new set with `hash_builder`.

This function is `const`, so it can be called in `static` contexts.

</div>

<div id="method.capacity" class="section method">

<a href="../../src/indexmap/set.rs.html#169-171"
class="src rightside">Source</a>

#### pub fn <a href="#method.capacity" class="fn">capacity</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Computes in **O(1)** time.

</div>

<div id="method.hasher" class="section method">

<a href="../../src/indexmap/set.rs.html#174-176"
class="src rightside">Source</a>

#### pub fn <a href="#method.hasher" class="fn">hasher</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;S</a>

</div>

<div class="docblock">

Return a reference to the set’s `BuildHasher`.

</div>

<div id="method.len" class="section method">

<a href="../../src/indexmap/set.rs.html#181-183"
class="src rightside">Source</a>

#### pub fn <a href="#method.len" class="fn">len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Return the number of elements in the set.

Computes in **O(1)** time.

</div>

<div id="method.is_empty" class="section method">

<a href="../../src/indexmap/set.rs.html#188-190"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_empty" class="fn">is_empty</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns true if the set contains no elements.

Computes in **O(1)** time.

</div>

<div id="method.iter" class="section method">

<a href="../../src/indexmap/set.rs.html#193-197"
class="src rightside">Source</a>

#### pub fn <a href="#method.iter" class="fn">iter</a>(&self) -\> <a href="struct.Iter.html" class="struct"
title="struct indexmap::set::Iter">Iter</a>\<'\_, T\> <a href="#" class="tooltip"
data-notable-ty="Iter&lt;&#39;_, T&gt;">ⓘ</a>

</div>

<div class="docblock">

Return an iterator over the values of the set, in their order

</div>

<div id="method.clear" class="section method">

<a href="../../src/indexmap/set.rs.html#202-204"
class="src rightside">Source</a>

#### pub fn <a href="#method.clear" class="fn">clear</a>(&mut self)

</div>

<div class="docblock">

Remove all elements in the set, while preserving its capacity.

Computes in **O(n)** time.

</div>

<div id="method.truncate" class="section method">

<a href="../../src/indexmap/set.rs.html#209-211"
class="src rightside">Source</a>

#### pub fn <a href="#method.truncate" class="fn">truncate</a>(&mut self, len: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Shortens the set, keeping the first `len` elements and dropping the
rest.

If `len` is greater than the set’s current length, this has no effect.

</div>

<div id="method.drain" class="section method">

<a href="../../src/indexmap/set.rs.html#226-233"
class="src rightside">Source</a>

#### pub fn <a href="#method.drain" class="fn">drain</a>\<R\>(&mut self, range: R) -\> <a href="struct.Drain.html" class="struct"
title="struct indexmap::set::Drain">Drain</a>\<'\_, T\> <a href="#" class="tooltip"
data-notable-ty="Drain&lt;&#39;_, T&gt;">ⓘ</a>

<div class="where">

where R: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/range/trait.RangeBounds.html"
class="trait"
title="trait core::ops::range::RangeBounds">RangeBounds</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\>,

</div>

</div>

<div class="docblock">

Clears the `IndexSet` in the given index range, returning those values
as a drain iterator.

The range may be any type that implements `RangeBounds<usize>`,
including all of the `std::ops::Range*` types, or even a tuple pair of
`Bound` start and end values. To drain the set entirely, use `RangeFull`
like `set.drain(..)`.

This shifts down all entries following the drained range to fill the
gap, and keeps the allocated memory for reuse.

***Panics*** if the starting point is greater than the end point or if
the end point is greater than the length of the set.

</div>

<div id="method.split_off" class="section method">

<a href="../../src/indexmap/set.rs.html#242-249"
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

Returns a newly allocated set containing the elements in the range
`[at, len)`. After the call, the original set will be left containing
the elements `[0, at)` with its previous capacity unchanged.

***Panics*** if `at > len`.

</div>

</div>

<div id="impl-IndexSet%3CT,+S%3E-1" class="section impl">

<a href="../../src/indexmap/set.rs.html#252-651"
class="src rightside">Source</a><a href="#impl-IndexSet%3CT,+S%3E-1" class="anchor">§</a>

### impl\<T, S\> <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where T:
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

<a href="../../src/indexmap/set.rs.html#260-262"
class="src rightside">Source</a>

#### pub fn <a href="#method.reserve" class="fn">reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Reserve capacity for `additional` more values.

Computes in **O(n)** time.

</div>

<div id="method.shrink_to_fit" class="section method">

<a href="../../src/indexmap/set.rs.html#267-269"
class="src rightside">Source</a>

#### pub fn <a href="#method.shrink_to_fit" class="fn">shrink_to_fit</a>(&mut self)

</div>

<div class="docblock">

Shrink the capacity of the set as much as possible.

Computes in **O(n)** time.

</div>

<div id="method.shrink_to" class="section method">

<a href="../../src/indexmap/set.rs.html#274-276"
class="src rightside">Source</a>

#### pub fn <a href="#method.shrink_to" class="fn">shrink_to</a>(&mut self, min_capacity: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Shrink the capacity of the set with a lower limit.

Computes in **O(n)** time.

</div>

<div id="method.insert" class="section method">

<a href="../../src/indexmap/set.rs.html#286-288"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(&mut self, value: T) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Insert the value into the set.

If an equivalent item already exists in the set, it returns `false`
leaving the original value in the set and without altering its insertion
order. Otherwise, it inserts the new item and returns `true`.

Computes in **O(1)** time (amortized average).

</div>

<div id="method.insert_full" class="section method">

<a href="../../src/indexmap/set.rs.html#299-310"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert_full" class="fn">insert_full</a>(&mut self, value: T) -\> (<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>)

</div>

<div class="docblock">

Insert the value into the set, and get its index.

If an equivalent item already exists in the set, it returns the index of
the existing item and `false`, leaving the original value in the set and
without altering its insertion order. Otherwise, it inserts the new item
and returns the index of the inserted item and `true`.

Computes in **O(1)** time (amortized average).

</div>

<div id="method.difference" class="section method">

<a href="../../src/indexmap/set.rs.html#315-323"
class="src rightside">Source</a>

#### pub fn <a href="#method.difference" class="fn">difference</a>\<'a, S2\>( &'a self, other: &'a <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>, ) -\> <a href="struct.Difference.html" class="struct"
title="struct indexmap::set::Difference">Difference</a>\<'a, T, S2\> <a href="#" class="tooltip"
data-notable-ty="Difference&lt;&#39;a, T, S2&gt;">ⓘ</a>

<div class="where">

where S2: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Return an iterator over the values that are in `self` but not `other`.

Values are produced in the same order that they appear in `self`.

</div>

<div id="method.symmetric_difference" class="section method">

<a href="../../src/indexmap/set.rs.html#330-340"
class="src rightside">Source</a>

#### pub fn <a href="#method.symmetric_difference"
class="fn">symmetric_difference</a>\<'a, S2\>( &'a self, other: &'a <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>, ) -\> <a href="struct.SymmetricDifference.html" class="struct"
title="struct indexmap::set::SymmetricDifference">SymmetricDifference</a>\<'a, T, S, S2\> <a href="#" class="tooltip"
data-notable-ty="SymmetricDifference&lt;&#39;a, T, S, S2&gt;">ⓘ</a>

<div class="where">

where S2: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Return an iterator over the values that are in `self` or `other`, but
not in both.

Values from `self` are produced in their original order, followed by
values from `other` in their original order.

</div>

<div id="method.intersection" class="section method">

<a href="../../src/indexmap/set.rs.html#345-353"
class="src rightside">Source</a>

#### pub fn <a href="#method.intersection" class="fn">intersection</a>\<'a, S2\>( &'a self, other: &'a <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>, ) -\> <a href="struct.Intersection.html" class="struct"
title="struct indexmap::set::Intersection">Intersection</a>\<'a, T, S2\> <a href="#" class="tooltip"
data-notable-ty="Intersection&lt;&#39;a, T, S2&gt;">ⓘ</a>

<div class="where">

where S2: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Return an iterator over the values that are in both `self` and `other`.

Values are produced in the same order that they appear in `self`.

</div>

<div id="method.union" class="section method">

<a href="../../src/indexmap/set.rs.html#359-366"
class="src rightside">Source</a>

#### pub fn <a href="#method.union" class="fn">union</a>\<'a, S2\>(&'a self, other: &'a <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>) -\> <a href="struct.Union.html" class="struct"
title="struct indexmap::set::Union">Union</a>\<'a, T, S\> <a href="#" class="tooltip"
data-notable-ty="Union&lt;&#39;a, T, S&gt;">ⓘ</a>

<div class="where">

where S2: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Return an iterator over all values that are in `self` or `other`.

Values from `self` are produced in their original order, followed by
values that are unique to `other` in their original order.

</div>

<div id="method.contains" class="section method">

<a href="../../src/indexmap/set.rs.html#371-376"
class="src rightside">Source</a>

#### pub fn <a href="#method.contains" class="fn">contains</a>\<Q\>(&self, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<T\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Return `true` if an equivalent to `value` exists in the set.

Computes in **O(1)** time (average).

</div>

<div id="method.get" class="section method">

<a href="../../src/indexmap/set.rs.html#382-387"
class="src rightside">Source</a>

#### pub fn <a href="#method.get" class="fn">get</a>\<Q\>(&self, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<T\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Return a reference to the value stored in the set, if it is present,
else `None`.

Computes in **O(1)** time (average).

</div>

<div id="method.get_full" class="section method">

<a href="../../src/indexmap/set.rs.html#390-395"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_full" class="fn">get_full</a>\<Q\>(&self, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>)\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<T\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Return item index and value

</div>

<div id="method.get_index_of" class="section method">

<a href="../../src/indexmap/set.rs.html#398-403"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_index_of" class="fn">get_index_of</a>\<Q\>(&self, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<T\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Return item index, if it exists in the set

</div>

<div id="method.replace" class="section method">

<a href="../../src/indexmap/set.rs.html#410-412"
class="src rightside">Source</a>

#### pub fn <a href="#method.replace" class="fn">replace</a>(&mut self, value: T) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div class="docblock">

Adds a value to the set, replacing the existing value, if any, that is
equal to the given one, without altering its insertion order. Returns
the replaced value.

Computes in **O(1)** time (average).

</div>

<div id="method.replace_full" class="section method">

<a href="../../src/indexmap/set.rs.html#419-430"
class="src rightside">Source</a>

#### pub fn <a href="#method.replace_full" class="fn">replace_full</a>(&mut self, value: T) -\> (<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>)

</div>

<div class="docblock">

Adds a value to the set, replacing the existing value, if any, that is
equal to the given one, without altering its insertion order. Returns
the index of the item and its replaced value.

Computes in **O(1)** time (average).

</div>

<div id="method.remove" class="section method">

<a href="../../src/indexmap/set.rs.html#438-443"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove" class="fn">remove</a>\<Q\>(&mut self, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<T\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Remove the value from the set, and return `true` if it was present.

**NOTE:** This is equivalent to `.swap_remove(value)`, if you want to
preserve the order of the values in the set, use `.shift_remove(value)`.

Computes in **O(1)** time (average).

</div>

<div id="method.swap_remove" class="section method">

<a href="../../src/indexmap/set.rs.html#454-459"
class="src rightside">Source</a>

#### pub fn <a href="#method.swap_remove" class="fn">swap_remove</a>\<Q\>(&mut self, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<T\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Remove the value from the set, and return `true` if it was present.

Like `Vec::swap_remove`, the value is removed by swapping it with the
last element of the set and popping it off. **This perturbs the position
of what used to be the last element!**

Return `false` if `value` was not in the set.

Computes in **O(1)** time (average).

</div>

<div id="method.shift_remove" class="section method">

<a href="../../src/indexmap/set.rs.html#470-475"
class="src rightside">Source</a>

#### pub fn <a href="#method.shift_remove" class="fn">shift_remove</a>\<Q\>(&mut self, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<T\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Remove the value from the set, and return `true` if it was present.

Like `Vec::remove`, the value is removed by shifting all of the elements
that follow it, preserving their relative order. **This perturbs the
index of all of those elements!**

Return `false` if `value` was not in the set.

Computes in **O(n)** time (average).

</div>

<div id="method.take" class="section method">

<a href="../../src/indexmap/set.rs.html#485-490"
class="src rightside">Source</a>

#### pub fn <a href="#method.take" class="fn">take</a>\<Q\>(&mut self, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<T\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Removes and returns the value in the set, if any, that is equal to the
given one.

**NOTE:** This is equivalent to `.swap_take(value)`, if you need to
preserve the order of the values in the set, use `.shift_take(value)`
instead.

Computes in **O(1)** time (average).

</div>

<div id="method.swap_take" class="section method">

<a href="../../src/indexmap/set.rs.html#502-507"
class="src rightside">Source</a>

#### pub fn <a href="#method.swap_take" class="fn">swap_take</a>\<Q\>(&mut self, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<T\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Removes and returns the value in the set, if any, that is equal to the
given one.

Like `Vec::swap_remove`, the value is removed by swapping it with the
last element of the set and popping it off. **This perturbs the position
of what used to be the last element!**

Return `None` if `value` was not in the set.

Computes in **O(1)** time (average).

</div>

<div id="method.shift_take" class="section method">

<a href="../../src/indexmap/set.rs.html#519-524"
class="src rightside">Source</a>

#### pub fn <a href="#method.shift_take" class="fn">shift_take</a>\<Q\>(&mut self, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<T\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Removes and returns the value in the set, if any, that is equal to the
given one.

Like `Vec::remove`, the value is removed by shifting all of the elements
that follow it, preserving their relative order. **This perturbs the
index of all of those elements!**

Return `None` if `value` was not in the set.

Computes in **O(n)** time (average).

</div>

<div id="method.swap_remove_full" class="section method">

<a href="../../src/indexmap/set.rs.html#533-538"
class="src rightside">Source</a>

#### pub fn <a href="#method.swap_remove_full" class="fn">swap_remove_full</a>\<Q\>(&mut self, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, T)\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<T\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Remove the value from the set return it and the index it had.

Like `Vec::swap_remove`, the value is removed by swapping it with the
last element of the set and popping it off. **This perturbs the position
of what used to be the last element!**

Return `None` if `value` was not in the set.

</div>

<div id="method.shift_remove_full" class="section method">

<a href="../../src/indexmap/set.rs.html#547-552"
class="src rightside">Source</a>

#### pub fn <a href="#method.shift_remove_full" class="fn">shift_remove_full</a>\<Q\>(&mut self, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, T)\>

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="../trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<T\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Remove the value from the set return it and the index it had.

Like `Vec::remove`, the value is removed by shifting all of the elements
that follow it, preserving their relative order. **This perturbs the
index of all of those elements!**

Return `None` if `value` was not in the set.

</div>

<div id="method.pop" class="section method">

<a href="../../src/indexmap/set.rs.html#559-561"
class="src rightside">Source</a>

#### pub fn <a href="#method.pop" class="fn">pop</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div class="docblock">

Remove the last value

This preserves the order of the remaining elements.

Computes in **O(1)** time (average).

</div>

<div id="method.retain" class="section method">

<a href="../../src/indexmap/set.rs.html#570-575"
class="src rightside">Source</a>

#### pub fn <a href="#method.retain" class="fn">retain</a>\<F\>(&mut self, keep: F)

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Scan through each value in the set and keep those where the closure
`keep` returns `true`.

The elements are visited in order, and remaining elements keep their
order.

Computes in **O(n)** time (average).

</div>

<div id="method.sort" class="section method">

<a href="../../src/indexmap/set.rs.html#580-585"
class="src rightside">Source</a>

#### pub fn <a href="#method.sort" class="fn">sort</a>(&mut self)

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html"
class="trait" title="trait core::cmp::Ord">Ord</a>,

</div>

</div>

<div class="docblock">

Sort the set’s values by their default ordering.

See
[`sort_by`](struct.IndexSet.html#method.sort_by "method indexmap::set::IndexSet::sort_by")
for details.

</div>

<div id="method.sort_by" class="section method">

<a href="../../src/indexmap/set.rs.html#590-595"
class="src rightside">Source</a>

#### pub fn <a href="#method.sort_by" class="fn">sort_by</a>\<F\>(&mut self, cmp: F)

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>,

</div>

</div>

<div class="docblock">

Sort the set’s values in place using the comparison function `cmp`.

Computes in **O(n log n)** time and **O(n)** space. The sort is stable.

</div>

<div id="method.sorted_by" class="section method">

<a href="../../src/indexmap/set.rs.html#601-610"
class="src rightside">Source</a>

#### pub fn <a href="#method.sorted_by" class="fn">sorted_by</a>\<F\>(self, cmp: F) -\> <a href="struct.IntoIter.html" class="struct"
title="struct indexmap::set::IntoIter">IntoIter</a>\<T\> <a href="#" class="tooltip" data-notable-ty="IntoIter&lt;T&gt;">ⓘ</a>

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>,

</div>

</div>

<div class="docblock">

Sort the values of the set and return a by-value iterator of the values
with the result.

The sort is stable.

</div>

<div id="method.sort_unstable" class="section method">

<a href="../../src/indexmap/set.rs.html#615-620"
class="src rightside">Source</a>

#### pub fn <a href="#method.sort_unstable" class="fn">sort_unstable</a>(&mut self)

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html"
class="trait" title="trait core::cmp::Ord">Ord</a>,

</div>

</div>

<div class="docblock">

Sort the set’s values by their default ordering.

See
[`sort_unstable_by`](struct.IndexSet.html#method.sort_unstable_by "method indexmap::set::IndexSet::sort_unstable_by")
for details.

</div>

<div id="method.sort_unstable_by" class="section method">

<a href="../../src/indexmap/set.rs.html#625-630"
class="src rightside">Source</a>

#### pub fn <a href="#method.sort_unstable_by" class="fn">sort_unstable_by</a>\<F\>(&mut self, cmp: F)

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>,

</div>

</div>

<div class="docblock">

Sort the set’s values in place using the comparison funtion `cmp`.

Computes in **O(n log n)** time. The sort is unstable.

</div>

<div id="method.sorted_unstable_by" class="section method">

<a href="../../src/indexmap/set.rs.html#634-643"
class="src rightside">Source</a>

#### pub fn <a href="#method.sorted_unstable_by" class="fn">sorted_unstable_by</a>\<F\>(self, cmp: F) -\> <a href="struct.IntoIter.html" class="struct"
title="struct indexmap::set::IntoIter">IntoIter</a>\<T\> <a href="#" class="tooltip" data-notable-ty="IntoIter&lt;T&gt;">ⓘ</a>

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>,

</div>

</div>

<div class="docblock">

Sort the values of the set and return a by-value iterator of the values
with the result.

</div>

<div id="method.reverse" class="section method">

<a href="../../src/indexmap/set.rs.html#648-650"
class="src rightside">Source</a>

#### pub fn <a href="#method.reverse" class="fn">reverse</a>(&mut self)

</div>

<div class="docblock">

Reverses the order of the set’s values in place.

Computes in **O(n)** time and **O(1)** space.

</div>

</div>

<div id="impl-IndexSet%3CT,+S%3E-2" class="section impl">

<a href="../../src/indexmap/set.rs.html#653-722"
class="src rightside">Source</a><a href="#impl-IndexSet%3CT,+S%3E-2" class="anchor">§</a>

### impl\<T, S\> <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

</div>

<div class="impl-items">

<div id="method.get_index" class="section method">

<a href="../../src/indexmap/set.rs.html#659-661"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_index" class="fn">get_index</a>(&self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>\>

</div>

<div class="docblock">

Get a value by index

Valid indices are *0 \<= index \< self.len()*

Computes in **O(1)** time.

</div>

<div id="method.first" class="section method">

<a href="../../src/indexmap/set.rs.html#666-668"
class="src rightside">Source</a>

#### pub fn <a href="#method.first" class="fn">first</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>\>

</div>

<div class="docblock">

Get the first value

Computes in **O(1)** time.

</div>

<div id="method.last" class="section method">

<a href="../../src/indexmap/set.rs.html#673-675"
class="src rightside">Source</a>

#### pub fn <a href="#method.last" class="fn">last</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>\>

</div>

<div class="docblock">

Get the last value

Computes in **O(1)** time.

</div>

<div id="method.swap_remove_index" class="section method">

<a href="../../src/indexmap/set.rs.html#686-688"
class="src rightside">Source</a>

#### pub fn <a href="#method.swap_remove_index" class="fn">swap_remove_index</a>(&mut self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div class="docblock">

Remove the value by index

Valid indices are *0 \<= index \< self.len()*

Like `Vec::swap_remove`, the value is removed by swapping it with the
last element of the set and popping it off. **This perturbs the position
of what used to be the last element!**

Computes in **O(1)** time (average).

</div>

<div id="method.shift_remove_index" class="section method">

<a href="../../src/indexmap/set.rs.html#699-701"
class="src rightside">Source</a>

#### pub fn <a href="#method.shift_remove_index" class="fn">shift_remove_index</a>(&mut self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div class="docblock">

Remove the value by index

Valid indices are *0 \<= index \< self.len()*

Like `Vec::remove`, the value is removed by shifting all of the elements
that follow it, preserving their relative order. **This perturbs the
index of all of those elements!**

Computes in **O(n)** time (average).

</div>

<div id="method.move_index" class="section method">

<a href="../../src/indexmap/set.rs.html#712-714"
class="src rightside">Source</a>

#### pub fn <a href="#method.move_index" class="fn">move_index</a>(&mut self, from: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, to: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Moves the position of a value from one index to another by shifting all
other values in-between.

- If `from < to`, the other values will shift down while the targeted
  value moves up.
- If `from > to`, the other values will shift up while the targeted
  value moves down.

***Panics*** if `from` or `to` are out of bounds.

Computes in **O(n)** time (average).

</div>

<div id="method.swap_indices" class="section method">

<a href="../../src/indexmap/set.rs.html#719-721"
class="src rightside">Source</a>

#### pub fn <a href="#method.swap_indices" class="fn">swap_indices</a>(&mut self, a: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, b: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Swaps the position of two values in the set.

***Panics*** if `a` or `b` are out of bounds.

</div>

</div>

<div id="impl-IndexSet%3CT,+S%3E-3" class="section impl">

<a href="../../src/indexmap/set.rs.html#983-1015"
class="src rightside">Source</a><a href="#impl-IndexSet%3CT,+S%3E-3" class="anchor">§</a>

### impl\<T, S\> <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="impl-items">

<div id="method.is_disjoint" class="section method">

<a href="../../src/indexmap/set.rs.html#989-998"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_disjoint" class="fn">is_disjoint</a>\<S2\>(&self, other: &<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where S2: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Returns `true` if `self` has no elements in common with `other`.

</div>

<div id="method.is_subset" class="section method">

<a href="../../src/indexmap/set.rs.html#1001-1006"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_subset" class="fn">is_subset</a>\<S2\>(&self, other: &<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where S2: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Returns `true` if all elements of `self` are contained in `other`.

</div>

<div id="method.is_superset" class="section method">

<a href="../../src/indexmap/set.rs.html#1009-1014"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_superset" class="fn">is_superset</a>\<S2\>(&self, other: &<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where S2: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="docblock">

Returns `true` if all elements of `other` are contained in `self`.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-BitAnd%3C%26IndexSet%3CT,+S2%3E%3E-for-%26IndexSet%3CT,+S1%3E"
class="section impl">

<a href="../../src/indexmap/set.rs.html#1321-1335"
class="src rightside">Source</a><a
href="#impl-BitAnd%3C%26IndexSet%3CT,+S2%3E%3E-for-%26IndexSet%3CT,+S1%3E"
class="anchor">§</a>

### impl\<T, S1, S2\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitAnd.html"
class="trait" title="trait core::ops::bit::BitAnd">BitAnd</a>\<&<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>\> for &<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S1\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, S1: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>, S2: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="impl-items">

<div id="method.bitand" class="section method trait-impl">

<a href="../../src/indexmap/set.rs.html#1332-1334"
class="src rightside">Source</a><a href="#method.bitand" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitAnd.html#tymethod.bitand"
class="fn">bitand</a>(self, other: &<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>) -\> Self::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitAnd.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::bit::BitAnd::Output">Output</a>

</div>

<div class="docblock">

Returns the set intersection, cloned into a new set.

Values are collected in the same order that they appear in `self`.

</div>

<div id="associatedtype.Output-1"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/set.rs.html#1327"
class="src rightside">Source</a><a href="#associatedtype.Output-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitAnd.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S1\>

</div>

<div class="docblock">

The resulting type after applying the `&` operator.

</div>

</div>

<div id="impl-BitOr%3C%26IndexSet%3CT,+S2%3E%3E-for-%26IndexSet%3CT,+S1%3E"
class="section impl">

<a href="../../src/indexmap/set.rs.html#1337-1352"
class="src rightside">Source</a><a
href="#impl-BitOr%3C%26IndexSet%3CT,+S2%3E%3E-for-%26IndexSet%3CT,+S1%3E"
class="anchor">§</a>

### impl\<T, S1, S2\> <a href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitOr.html"
class="trait" title="trait core::ops::bit::BitOr">BitOr</a>\<&<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>\> for &<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S1\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, S1: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>, S2: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="impl-items">

<div id="method.bitor" class="section method trait-impl">

<a href="../../src/indexmap/set.rs.html#1349-1351"
class="src rightside">Source</a><a href="#method.bitor" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitOr.html#tymethod.bitor"
class="fn">bitor</a>(self, other: &<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>) -\> Self::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitOr.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::bit::BitOr::Output">Output</a>

</div>

<div class="docblock">

Returns the set union, cloned into a new set.

Values from `self` are collected in their original order, followed by
values that are unique to `other` in their original order.

</div>

<div id="associatedtype.Output-2"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/set.rs.html#1343"
class="src rightside">Source</a><a href="#associatedtype.Output-2" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitOr.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S1\>

</div>

<div class="docblock">

The resulting type after applying the `|` operator.

</div>

</div>

<div id="impl-BitXor%3C%26IndexSet%3CT,+S2%3E%3E-for-%26IndexSet%3CT,+S1%3E"
class="section impl">

<a href="../../src/indexmap/set.rs.html#1354-1369"
class="src rightside">Source</a><a
href="#impl-BitXor%3C%26IndexSet%3CT,+S2%3E%3E-for-%26IndexSet%3CT,+S1%3E"
class="anchor">§</a>

### impl\<T, S1, S2\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitXor.html"
class="trait" title="trait core::ops::bit::BitXor">BitXor</a>\<&<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>\> for &<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S1\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, S1: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>, S2: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="impl-items">

<div id="method.bitxor" class="section method trait-impl">

<a href="../../src/indexmap/set.rs.html#1366-1368"
class="src rightside">Source</a><a href="#method.bitxor" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitXor.html#tymethod.bitxor"
class="fn">bitxor</a>(self, other: &<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>) -\> Self::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitXor.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::bit::BitXor::Output">Output</a>

</div>

<div class="docblock">

Returns the set symmetric-difference, cloned into a new set.

Values from `self` are collected in their original order, followed by
values from `other` in their original order.

</div>

<div id="associatedtype.Output-3"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/set.rs.html#1360"
class="src rightside">Source</a><a href="#associatedtype.Output-3" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitXor.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S1\>

</div>

<div class="docblock">

The resulting type after applying the `^` operator.

</div>

</div>

<div id="impl-Clone-for-IndexSet%3CT,+S%3E" class="section impl">

<a href="../../src/indexmap/set.rs.html#71-85"
class="src rightside">Source</a><a href="#impl-Clone-for-IndexSet%3CT,+S%3E" class="anchor">§</a>

### impl\<T, S\> <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, S:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../../src/indexmap/set.rs.html#76-80"
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

<a href="../../src/indexmap/set.rs.html#82-84"
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

<div id="impl-Debug-for-IndexSet%3CT,+S%3E" class="section impl">

<a href="../../src/indexmap/set.rs.html#113-125"
class="src rightside">Source</a><a href="#impl-Debug-for-IndexSet%3CT,+S%3E" class="anchor">§</a>

### impl\<T, S\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>,

</div>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../../src/indexmap/set.rs.html#117-124"
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

<div id="impl-Default-for-IndexSet%3CT,+S%3E" class="section impl">

<a href="../../src/indexmap/set.rs.html#953-963"
class="src rightside">Source</a><a href="#impl-Default-for-IndexSet%3CT,+S%3E" class="anchor">§</a>

### impl\<T, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where S: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>,

</div>

</div>

<div class="impl-items">

<div id="method.default" class="section method trait-impl">

<a href="../../src/indexmap/set.rs.html#958-962"
class="src rightside">Source</a><a href="#method.default" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html#tymethod.default"
class="fn">default</a>() -\> Self

</div>

<div class="docblock">

Return an empty `IndexSet`

</div>

</div>

<div id="impl-Extend%3C%26T%3E-for-IndexSet%3CT,+S%3E"
class="section impl">

<a href="../../src/indexmap/set.rs.html#942-951"
class="src rightside">Source</a><a href="#impl-Extend%3C%26T%3E-for-IndexSet%3CT,+S%3E"
class="anchor">§</a>

### impl\<'a, T, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T</a>\> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a> + 'a, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="impl-items">

<div id="method.extend-1" class="section method trait-impl">

<a href="../../src/indexmap/set.rs.html#947-950"
class="src rightside">Source</a><a href="#method.extend-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T</a>\>\>(&mut self, iterable: I)

</div>

<div class="docblock">

Extends a collection with the contents of an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend)

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

<div id="impl-Extend%3CT%3E-for-IndexSet%3CT,+S%3E"
class="section impl">

<a href="../../src/indexmap/set.rs.html#931-940"
class="src rightside">Source</a><a href="#impl-Extend%3CT%3E-for-IndexSet%3CT,+S%3E"
class="anchor">§</a>

### impl\<T, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<T\> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where T:
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

<a href="../../src/indexmap/set.rs.html#936-939"
class="src rightside">Source</a><a href="#method.extend" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = T\>\>(&mut self, iterable: I)

</div>

<div class="docblock">

Extends a collection with the contents of an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend)

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

<div id="impl-From%3C%5BT;+N%5D%3E-for-IndexSet%3CT%3E"
class="section impl">

<a href="../../src/indexmap/set.rs.html#913-929"
class="src rightside">Source</a><a href="#impl-From%3C%5BT;+N%5D%3E-for-IndexSet%3CT%3E"
class="anchor">§</a>

### impl\<T, const N: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.array.html"
class="primitive">[T; N]</a>\> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, <a
href="https://doc.rust-lang.org/1.92.0/std/hash/random/struct.RandomState.html"
class="struct"
title="struct std::hash::random::RandomState">RandomState</a>\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>,

</div>

<span class="item-info"></span>

<div class="stab portability">

Available on **`has_std`** only.

</div>

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a href="../../src/indexmap/set.rs.html#926-928"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(arr: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.array.html"
class="primitive">[T; N]</a>) -\> Self

</div>

<div class="docblock">

##### <a href="#examples-2" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use indexmap::IndexSet;

let set1 = IndexSet::from([1, 2, 3, 4]);
let set2: IndexSet<_> = [1, 2, 3, 4].into();
assert_eq!(set1, set2);
```

</div>

</div>

</div>

<div id="impl-FromIterator%3CT%3E-for-IndexSet%3CT,+S%3E"
class="section impl">

<a href="../../src/indexmap/set.rs.html#899-910"
class="src rightside">Source</a><a href="#impl-FromIterator%3CT%3E-for-IndexSet%3CT,+S%3E"
class="anchor">§</a>

### impl\<T, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html"
class="trait"
title="trait core::iter::traits::collect::FromIterator">FromIterator</a>\<T\> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where T:
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

<a href="../../src/indexmap/set.rs.html#904-909"
class="src rightside">Source</a><a href="#method.from_iter" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html#tymethod.from_iter"
class="fn">from_iter</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = T\>\>(iterable: I) -\> Self

</div>

<div class="docblock">

Creates a value from an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html#tymethod.from_iter)

</div>

</div>

<div id="impl-Index%3Cusize%3E-for-IndexSet%3CT,+S%3E"
class="section impl">

<a href="../../src/indexmap/set.rs.html#752-762"
class="src rightside">Source</a><a href="#impl-Index%3Cusize%3E-for-IndexSet%3CT,+S%3E"
class="anchor">§</a>

### impl\<T, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html"
class="trait" title="trait core::ops::index::Index">Index</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="docblock">

Access `IndexSet` values at indexed positions.

</div>

</div>

<div class="docblock">

#### <a href="#examples-1" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use indexmap::IndexSet;

let mut set = IndexSet::new();
for word in "Lorem ipsum dolor sit amet".split_whitespace() {
    set.insert(word.to_string());
}
assert_eq!(set[0], "Lorem");
assert_eq!(set[1], "ipsum");
set.reverse();
assert_eq!(set[0], "amet");
assert_eq!(set[1], "sit");
set.sort();
assert_eq!(set[0], "Lorem");
assert_eq!(set[1], "amet");
```

</div>

<div class="example-wrap should_panic">

<a href="#" class="tooltip" title="This example panics">ⓘ</a>

``` rust
use indexmap::IndexSet;

let mut set = IndexSet::new();
set.insert("foo");
println!("{:?}", set[10]); // panics!
```

</div>

</div>

<div class="impl-items">

<div id="method.index" class="section method trait-impl">

<a href="../../src/indexmap/set.rs.html#758-761"
class="src rightside">Source</a><a href="#method.index" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html#tymethod.index"
class="fn">index</a>(&self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="docblock">

Returns a reference to the value at the supplied `index`.

***Panics*** if `index` is out of bounds.

</div>

<div id="associatedtype.Output"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/set.rs.html#753"
class="src rightside">Source</a><a href="#associatedtype.Output" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html#associatedtype.Output"
class="associatedtype">Output</a> = T

</div>

<div class="docblock">

The returned type after indexing.

</div>

</div>

<div id="impl-IntoIterator-for-%26IndexSet%3CT,+S%3E"
class="section impl">

<a href="../../src/indexmap/set.rs.html#879-886"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-%26IndexSet%3CT,+S%3E"
class="anchor">§</a>

### impl\<'a, T, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for &'a <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

</div>

<div class="impl-items">

<div id="associatedtype.Item" class="section associatedtype trait-impl">

<a href="../../src/indexmap/set.rs.html#880"
class="src rightside">Source</a><a href="#associatedtype.Item" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T</a>

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/set.rs.html#881"
class="src rightside">Source</a><a href="#associatedtype.IntoIter" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="struct.Iter.html" class="struct"
title="struct indexmap::set::Iter">Iter</a>\<'a, T\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

<div id="method.into_iter" class="section method trait-impl">

<a href="../../src/indexmap/set.rs.html#883-885"
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

<div id="impl-IntoIterator-for-IndexSet%3CT,+S%3E" class="section impl">

<a href="../../src/indexmap/set.rs.html#888-897"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-IndexSet%3CT,+S%3E" class="anchor">§</a>

### impl\<T, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

</div>

<div class="impl-items">

<div id="associatedtype.Item-1"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/set.rs.html#889"
class="src rightside">Source</a><a href="#associatedtype.Item-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = T

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter-1"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/set.rs.html#890"
class="src rightside">Source</a><a href="#associatedtype.IntoIter-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="struct.IntoIter.html" class="struct"
title="struct indexmap::set::IntoIter">IntoIter</a>\<T\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

<div id="method.into_iter-1" class="section method trait-impl">

<a href="../../src/indexmap/set.rs.html#892-896"
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

<div id="impl-PartialEq%3CIndexSet%3CT,+S2%3E%3E-for-IndexSet%3CT,+S1%3E"
class="section impl">

<a href="../../src/indexmap/set.rs.html#965-974"
class="src rightside">Source</a><a
href="#impl-PartialEq%3CIndexSet%3CT,+S2%3E%3E-for-IndexSet%3CT,+S1%3E"
class="anchor">§</a>

### impl\<T, S1, S2\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a>\<<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>\> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S1\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a>, S1: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>, S2:
<a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../../src/indexmap/set.rs.html#971-973"
class="src rightside">Source</a><a href="#method.eq" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#tymethod.eq"
class="fn">eq</a>(&self, other: &<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
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

<div id="impl-Sub%3C%26IndexSet%3CT,+S2%3E%3E-for-%26IndexSet%3CT,+S1%3E"
class="section impl">

<a href="../../src/indexmap/set.rs.html#1371-1385"
class="src rightside">Source</a><a
href="#impl-Sub%3C%26IndexSet%3CT,+S2%3E%3E-for-%26IndexSet%3CT,+S1%3E"
class="anchor">§</a>

### impl\<T, S1, S2\> <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Sub.html"
class="trait" title="trait core::ops::arith::Sub">Sub</a>\<&<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>\> for &<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S1\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, S1: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>, S2: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

<div class="impl-items">

<div id="method.sub" class="section method trait-impl">

<a href="../../src/indexmap/set.rs.html#1382-1384"
class="src rightside">Source</a><a href="#method.sub" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Sub.html#tymethod.sub"
class="fn">sub</a>(self, other: &<a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S2\>) -\> Self::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Sub.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::arith::Sub::Output">Output</a>

</div>

<div class="docblock">

Returns the set difference, cloned into a new set.

Values are collected in the same order that they appear in `self`.

</div>

<div id="associatedtype.Output-4"
class="section associatedtype trait-impl">

<a href="../../src/indexmap/set.rs.html#1377"
class="src rightside">Source</a><a href="#associatedtype.Output-4" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Sub.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S1\>

</div>

<div class="docblock">

The resulting type after applying the `-` operator.

</div>

</div>

<div id="impl-Eq-for-IndexSet%3CT,+S%3E" class="section impl">

<a href="../../src/indexmap/set.rs.html#976-981"
class="src rightside">Source</a><a href="#impl-Eq-for-IndexSet%3CT,+S%3E" class="anchor">§</a>

### impl\<T, S\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>,

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-IndexSet%3CT,+S%3E" class="section impl">

<a href="#impl-Freeze-for-IndexSet%3CT,+S%3E" class="anchor">§</a>

### impl\<T, S\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>,

</div>

</div>

<div id="impl-RefUnwindSafe-for-IndexSet%3CT,+S%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-IndexSet%3CT,+S%3E"
class="anchor">§</a>

### impl\<T, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where S: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
T: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

<div id="impl-Send-for-IndexSet%3CT,+S%3E" class="section impl">

<a href="#impl-Send-for-IndexSet%3CT,+S%3E" class="anchor">§</a>

### impl\<T, S\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-IndexSet%3CT,+S%3E" class="section impl">

<a href="#impl-Sync-for-IndexSet%3CT,+S%3E" class="anchor">§</a>

### impl\<T, S\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>,

</div>

</div>

<div id="impl-Unpin-for-IndexSet%3CT,+S%3E" class="section impl">

<a href="#impl-Unpin-for-IndexSet%3CT,+S%3E" class="anchor">§</a>

### impl\<T, S\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-IndexSet%3CT,+S%3E" class="section impl">

<a href="#impl-UnwindSafe-for-IndexSet%3CT,+S%3E" class="anchor">§</a>

### impl\<T, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.IndexSet.html" class="struct"
title="struct indexmap::set::IndexSet">IndexSet</a>\<T, S\>

<div class="where">

where S: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a>, T: <a
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
