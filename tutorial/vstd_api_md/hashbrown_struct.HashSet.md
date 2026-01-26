<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[hashbrown](index.html)

</div>

# Struct <span class="struct">HashSet</span> Copy item path

<span class="sub-heading"><a href="../src/hashbrown/set.rs.html#115-117" class="src">Source</a>
</span>

</div>

``` rust
pub struct HashSet<T, S = DefaultHashBuilder, A: Allocator + Clone = Global> { /* private fields */ }
```

Expand description

<div class="docblock">

A hash set implemented as a `HashMap` where the value is `()`.

As with the [`HashMap`](struct.HashMap.html) type, a `HashSet` requires
that the elements implement the
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) and
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) traits.
This can frequently be achieved by using
`#[derive(PartialEq, Eq, Hash)]`. If you implement these yourself, it is
important that the following property holds:

<div class="example-wrap">

``` text
k1 == k2 -> hash(k1) == hash(k2)
```

</div>

In other words, if two keys are equal, their hashes must be equal.

It is a logic error for an item to be modified in such a way that the
item’s hash, as determined by the
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) trait, or
its equality, as determined by the
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) trait, changes
while it is in the set. This is normally only possible through
[`Cell`](https://doc.rust-lang.org/std/cell/struct.Cell.html),
[`RefCell`](https://doc.rust-lang.org/std/cell/struct.RefCell.html),
global state, I/O, or unsafe code.

It is also a logic error for the
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html)
implementation of a key to panic. This is generally only possible if the
trait is implemented manually. If a panic does occur then the contents
of the `HashSet` may become corrupted and some items may be dropped from
the table.

## <a href="#examples" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
// Type inference lets us omit an explicit type signature (which
// would be `HashSet<String>` in this example).
let mut books = HashSet::new();

// Add some books.
books.insert("A Dance With Dragons".to_string());
books.insert("To Kill a Mockingbird".to_string());
books.insert("The Odyssey".to_string());
books.insert("The Great Gatsby".to_string());

// Check for a specific one.
if !books.contains("The Winds of Winter") {
    println!("We have {} books, but The Winds of Winter ain't one.",
             books.len());
}

// Remove a book.
books.remove("The Odyssey");

// Iterate over everything.
for book in &books {
    println!("{}", book);
}
```

</div>

The easiest way to use `HashSet` with a custom type is to derive
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) and
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html). We must
also derive
[`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html).
This will in the future be implied by
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html).

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
#[derive(Hash, Eq, PartialEq, Debug)]
struct Viking {
    name: String,
    power: usize,
}

let mut vikings = HashSet::new();

vikings.insert(Viking { name: "Einar".to_string(), power: 9 });
vikings.insert(Viking { name: "Einar".to_string(), power: 9 });
vikings.insert(Viking { name: "Olaf".to_string(), power: 4 });
vikings.insert(Viking { name: "Harald".to_string(), power: 8 });

// Use derived implementation to print the vikings.
for x in &vikings {
    println!("{:?}", x);
}
```

</div>

A `HashSet` with fixed list of elements can be initialized from an
array:

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let viking_names: HashSet<&'static str> =
    [ "Einar", "Olaf", "Harald" ].iter().cloned().collect();
// use the values stored in the set
```

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-HashSet%3CT,+S,+A%3E" class="section impl">

<a href="../src/hashbrown/set.rs.html#211-383"
class="src rightside">Source</a><a href="#impl-HashSet%3CT,+S,+A%3E" class="anchor">§</a>

### impl\<T, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

</div>

<div class="impl-items">

<div id="method.capacity" class="section method">

<a href="../src/hashbrown/set.rs.html#222-224"
class="src rightside">Source</a>

#### pub fn <a href="#method.capacity" class="fn">capacity</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Returns the number of elements the set can hold without reallocating.

##### <a href="#examples-1" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
let set: HashSet<i32> = HashSet::with_capacity(100);
assert!(set.capacity() >= 100);
```

</div>

</div>

<div id="method.iter" class="section method">

<a href="../src/hashbrown/set.rs.html#243-247"
class="src rightside">Source</a>

#### pub fn <a href="#method.iter" class="fn">iter</a>(&self) -\> <a href="hash_set/struct.Iter.html" class="struct"
title="struct hashbrown::hash_set::Iter">Iter</a>\<'\_, T\> <a href="#" class="tooltip"
data-notable-ty="Iter&lt;&#39;_, T&gt;">ⓘ</a>

</div>

<div class="docblock">

An iterator visiting all elements in arbitrary order. The iterator
element type is `&'a T`.

##### <a href="#examples-2" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
let mut set = HashSet::new();
set.insert("a");
set.insert("b");

// Will print in an arbitrary order.
for x in set.iter() {
    println!("{}", x);
}
```

</div>

</div>

<div id="method.len" class="section method">

<a href="../src/hashbrown/set.rs.html#262-264"
class="src rightside">Source</a>

#### pub fn <a href="#method.len" class="fn">len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Returns the number of elements in the set.

##### <a href="#examples-3" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut v = HashSet::new();
assert_eq!(v.len(), 0);
v.insert(1);
assert_eq!(v.len(), 1);
```

</div>

</div>

<div id="method.is_empty" class="section method">

<a href="../src/hashbrown/set.rs.html#279-281"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_empty" class="fn">is_empty</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns `true` if the set contains no elements.

##### <a href="#examples-4" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut v = HashSet::new();
assert!(v.is_empty());
v.insert(1);
assert!(!v.is_empty());
```

</div>

</div>

<div id="method.drain" class="section method">

<a href="../src/hashbrown/set.rs.html#301-305"
class="src rightside">Source</a>

#### pub fn <a href="#method.drain" class="fn">drain</a>(&mut self) -\> <a href="hash_set/struct.Drain.html" class="struct"
title="struct hashbrown::hash_set::Drain">Drain</a>\<'\_, T, A\> <a href="#" class="tooltip"
data-notable-ty="Drain&lt;&#39;_, T, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Clears the set, returning all elements in an iterator.

##### <a href="#examples-5" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut set: HashSet<_> = [1, 2, 3].iter().cloned().collect();
assert!(!set.is_empty());

// print 1, 2, 3 in an arbitrary order
for i in set.drain() {
    println!("{}", i);
}

assert!(set.is_empty());
```

</div>

</div>

<div id="method.retain" class="section method">

<a href="../src/hashbrown/set.rs.html#321-326"
class="src rightside">Source</a>

#### pub fn <a href="#method.retain" class="fn">retain</a>\<F\>(&mut self, f: F)

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Retains only the elements specified by the predicate.

In other words, remove all elements `e` such that `f(&e)` returns
`false`.

##### <a href="#examples-6" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let xs = [1,2,3,4,5,6];
let mut set: HashSet<i32> = xs.iter().cloned().collect();
set.retain(|&k| k % 2 == 0);
assert_eq!(set.len(), 3);
```

</div>

</div>

<div id="method.drain_filter" class="section method">

<a href="../src/hashbrown/set.rs.html#354-365"
class="src rightside">Source</a>

#### pub fn <a href="#method.drain_filter" class="fn">drain_filter</a>\<F\>(&mut self, f: F) -\> <a href="hash_set/struct.DrainFilter.html" class="struct"
title="struct hashbrown::hash_set::DrainFilter">DrainFilter</a>\<'\_, T, F, A\> <a href="#" class="tooltip"
data-notable-ty="DrainFilter&lt;&#39;_, T, F, A&gt;">ⓘ</a>

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Drains elements which are true under the given predicate, and returns an
iterator over the removed items.

In other words, move all elements `e` such that `f(&e)` returns `true`
out into another iterator.

When the returned DrainedFilter is dropped, any remaining elements that
satisfy the predicate are dropped from the set.

##### <a href="#examples-7" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut set: HashSet<i32> = (0..8).collect();
let drained: HashSet<i32> = set.drain_filter(|v| v % 2 == 0).collect();

let mut evens = drained.into_iter().collect::<Vec<_>>();
let mut odds = set.into_iter().collect::<Vec<_>>();
evens.sort();
odds.sort();

assert_eq!(evens, vec![0, 2, 4, 6]);
assert_eq!(odds, vec![1, 3, 5, 7]);
```

</div>

</div>

<div id="method.clear" class="section method">

<a href="../src/hashbrown/set.rs.html#380-382"
class="src rightside">Source</a>

#### pub fn <a href="#method.clear" class="fn">clear</a>(&mut self)

</div>

<div class="docblock">

Clears the set, removing all values.

##### <a href="#examples-8" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut v = HashSet::new();
v.insert(1);
v.clear();
assert!(v.is_empty());
```

</div>

</div>

</div>

<div id="impl-HashSet%3CT,+S%3E" class="section impl">

<a href="../src/hashbrown/set.rs.html#385-451"
class="src rightside">Source</a><a href="#impl-HashSet%3CT,+S%3E" class="anchor">§</a>

### impl\<T, S\> <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, Global\>

</div>

<div class="impl-items">

<div id="method.with_hasher" class="section method">

<a href="../src/hashbrown/set.rs.html#413-417"
class="src rightside">Source</a>

#### pub const fn <a href="#method.with_hasher" class="fn">with_hasher</a>(hasher: S) -\> Self

</div>

<div class="docblock">

Creates a new empty hash set which will use the given hasher to hash
keys.

The hash set is also created with the default initial capacity.

Warning: `hasher` is normally randomly generated, and is designed to
allow `HashSet`s to be resistant to attacks that cause many collisions
and very poor performance. Setting it manually using this function can
expose a DoS attack vector.

The `hash_builder` passed should implement the
[`BuildHasher`](../../std/hash/trait.BuildHasher.html) trait for the
HashMap to be useful, see its documentation for details.

##### <a href="#examples-9" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
use hashbrown::hash_map::DefaultHashBuilder;

let s = DefaultHashBuilder::default();
let mut set = HashSet::with_hasher(s);
set.insert(2);
```

</div>

</div>

<div id="method.with_capacity_and_hasher" class="section method">

<a href="../src/hashbrown/set.rs.html#446-450"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_capacity_and_hasher"
class="fn">with_capacity_and_hasher</a>(capacity: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>, hasher: S) -\> Self

</div>

<div class="docblock">

Creates an empty `HashSet` with the specified capacity, using `hasher`
to hash the keys.

The hash set will be able to hold at least `capacity` elements without
reallocating. If `capacity` is 0, the hash set will not allocate.

Warning: `hasher` is normally randomly generated, and is designed to
allow `HashSet`s to be resistant to attacks that cause many collisions
and very poor performance. Setting it manually using this function can
expose a DoS attack vector.

The `hash_builder` passed should implement the
[`BuildHasher`](../../std/hash/trait.BuildHasher.html) trait for the
HashMap to be useful, see its documentation for details.

##### <a href="#examples-10" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
use hashbrown::hash_map::DefaultHashBuilder;

let s = DefaultHashBuilder::default();
let mut set = HashSet::with_capacity_and_hasher(10, s);
set.insert(1);
```

</div>

</div>

</div>

<div id="impl-HashSet%3CT,+S,+A%3E-1" class="section impl">

<a href="../src/hashbrown/set.rs.html#453-536"
class="src rightside">Source</a><a href="#impl-HashSet%3CT,+S,+A%3E-1" class="anchor">§</a>

### impl\<T, S, A\> <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where A: Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.allocator" class="section method">

<a href="../src/hashbrown/set.rs.html#459-461"
class="src rightside">Source</a>

#### pub fn <a href="#method.allocator" class="fn">allocator</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;A</a>

</div>

<div class="docblock">

Returns a reference to the underlying allocator.

</div>

<div id="method.with_hasher_in" class="section method">

<a href="../src/hashbrown/set.rs.html#484-488"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_hasher_in" class="fn">with_hasher_in</a>(hasher: S, alloc: A) -\> Self

</div>

<div class="docblock">

Creates a new empty hash set which will use the given hasher to hash
keys.

The hash set is also created with the default initial capacity.

Warning: `hasher` is normally randomly generated, and is designed to
allow `HashSet`s to be resistant to attacks that cause many collisions
and very poor performance. Setting it manually using this function can
expose a DoS attack vector.

##### <a href="#examples-11" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
use hashbrown::hash_map::DefaultHashBuilder;

let s = DefaultHashBuilder::default();
let mut set = HashSet::with_hasher(s);
set.insert(2);
```

</div>

</div>

<div id="method.with_capacity_and_hasher_in" class="section method">

<a href="../src/hashbrown/set.rs.html#512-516"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_capacity_and_hasher_in"
class="fn">with_capacity_and_hasher_in</a>(capacity: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>, hasher: S, alloc: A) -\> Self

</div>

<div class="docblock">

Creates an empty `HashSet` with the specified capacity, using `hasher`
to hash the keys.

The hash set will be able to hold at least `capacity` elements without
reallocating. If `capacity` is 0, the hash set will not allocate.

Warning: `hasher` is normally randomly generated, and is designed to
allow `HashSet`s to be resistant to attacks that cause many collisions
and very poor performance. Setting it manually using this function can
expose a DoS attack vector.

##### <a href="#examples-12" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
use hashbrown::hash_map::DefaultHashBuilder;

let s = DefaultHashBuilder::default();
let mut set = HashSet::with_capacity_and_hasher(10, s);
set.insert(1);
```

</div>

</div>

<div id="method.hasher" class="section method">

<a href="../src/hashbrown/set.rs.html#533-535"
class="src rightside">Source</a>

#### pub fn <a href="#method.hasher" class="fn">hasher</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;S</a>

</div>

<div class="docblock">

Returns a reference to the set’s
[`BuildHasher`](https://doc.rust-lang.org/std/hash/trait.BuildHasher.html).

##### <a href="#examples-13" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
use hashbrown::hash_map::DefaultHashBuilder;

let hasher = DefaultHashBuilder::default();
let set: HashSet<i32> = HashSet::with_hasher(hasher);
let hasher: &DefaultHashBuilder = set.hasher();
```

</div>

</div>

</div>

<div id="impl-HashSet%3CT,+S,+A%3E-2" class="section impl">

<a href="../src/hashbrown/set.rs.html#538-1145"
class="src rightside">Source</a><a href="#impl-HashSet%3CT,+S,+A%3E-2" class="anchor">§</a>

### impl\<T, S, A\> <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>, A:
Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.reserve" class="section method">

<a href="../src/hashbrown/set.rs.html#561-563"
class="src rightside">Source</a>

#### pub fn <a href="#method.reserve" class="fn">reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Reserves capacity for at least `additional` more elements to be inserted
in the `HashSet`. The collection may reserve more space to avoid
frequent reallocations.

##### <a href="#panics" class="doc-anchor">§</a>Panics

Panics if the new allocation size overflows `usize`.

##### <a href="#examples-14" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
let mut set: HashSet<i32> = HashSet::new();
set.reserve(10);
assert!(set.capacity() >= 10);
```

</div>

</div>

<div id="method.try_reserve" class="section method">

<a href="../src/hashbrown/set.rs.html#582-584"
class="src rightside">Source</a>

#### pub fn <a href="#method.try_reserve" class="fn">try_reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.unit.html"
class="primitive">()</a>, <a href="enum.TryReserveError.html" class="enum"
title="enum hashbrown::TryReserveError">TryReserveError</a>\>

</div>

<div class="docblock">

Tries to reserve capacity for at least `additional` more elements to be
inserted in the given `HashSet<K,V>`. The collection may reserve more
space to avoid frequent reallocations.

##### <a href="#errors" class="doc-anchor">§</a>Errors

If the capacity overflows, or the allocator reports a failure, then an
error is returned.

##### <a href="#examples-15" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
let mut set: HashSet<i32> = HashSet::new();
set.try_reserve(10).expect("why is the test harness OOMing on 10 bytes?");
```

</div>

</div>

<div id="method.shrink_to_fit" class="section method">

<a href="../src/hashbrown/set.rs.html#603-605"
class="src rightside">Source</a>

#### pub fn <a href="#method.shrink_to_fit" class="fn">shrink_to_fit</a>(&mut self)

</div>

<div class="docblock">

Shrinks the capacity of the set as much as possible. It will drop down
as much as possible while maintaining the internal rules and possibly
leaving some space in accordance with the resize policy.

##### <a href="#examples-16" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut set = HashSet::with_capacity(100);
set.insert(1);
set.insert(2);
assert!(set.capacity() >= 100);
set.shrink_to_fit();
assert!(set.capacity() >= 2);
```

</div>

</div>

<div id="method.shrink_to" class="section method">

<a href="../src/hashbrown/set.rs.html#629-631"
class="src rightside">Source</a>

#### pub fn <a href="#method.shrink_to" class="fn">shrink_to</a>(&mut self, min_capacity: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Shrinks the capacity of the set with a lower limit. It will drop down no
lower than the supplied limit while maintaining the internal rules and
possibly leaving some space in accordance with the resize policy.

Panics if the current capacity is smaller than the supplied minimum
capacity.

##### <a href="#examples-17" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut set = HashSet::with_capacity(100);
set.insert(1);
set.insert(2);
assert!(set.capacity() >= 100);
set.shrink_to(10);
assert!(set.capacity() >= 10);
set.shrink_to(0);
assert!(set.capacity() >= 2);
```

</div>

</div>

<div id="method.difference" class="section method">

<a href="../src/hashbrown/set.rs.html#657-662"
class="src rightside">Source</a>

#### pub fn <a href="#method.difference" class="fn">difference</a>\<'a\>(&'a self, other: &'a Self) -\> <a href="hash_set/struct.Difference.html" class="struct"
title="struct hashbrown::hash_set::Difference">Difference</a>\<'a, T, S, A\> <a href="#" class="tooltip"
data-notable-ty="Difference&lt;&#39;a, T, S, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Visits the values representing the difference, i.e., the values that are
in `self` but not in `other`.

##### <a href="#examples-18" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
let a: HashSet<_> = [1, 2, 3].iter().cloned().collect();
let b: HashSet<_> = [4, 2, 3, 4].iter().cloned().collect();

// Can be seen as `a - b`.
for x in a.difference(&b) {
    println!("{}", x); // Print 1
}

let diff: HashSet<_> = a.difference(&b).collect();
assert_eq!(diff, [1].iter().collect());

// Note that difference is not symmetric,
// and `b - a` means something else:
let diff: HashSet<_> = b.difference(&a).collect();
assert_eq!(diff, [4].iter().collect());
```

</div>

</div>

<div id="method.symmetric_difference" class="section method">

<a href="../src/hashbrown/set.rs.html#686-690"
class="src rightside">Source</a>

#### pub fn <a href="#method.symmetric_difference"
class="fn">symmetric_difference</a>\<'a\>( &'a self, other: &'a Self, ) -\> <a href="hash_set/struct.SymmetricDifference.html" class="struct"
title="struct hashbrown::hash_set::SymmetricDifference">SymmetricDifference</a>\<'a, T, S, A\> <a href="#" class="tooltip"
data-notable-ty="SymmetricDifference&lt;&#39;a, T, S, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Visits the values representing the symmetric difference, i.e., the
values that are in `self` or in `other` but not in both.

##### <a href="#examples-19" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
let a: HashSet<_> = [1, 2, 3].iter().cloned().collect();
let b: HashSet<_> = [4, 2, 3, 4].iter().cloned().collect();

// Print 1, 4 in arbitrary order.
for x in a.symmetric_difference(&b) {
    println!("{}", x);
}

let diff1: HashSet<_> = a.symmetric_difference(&b).collect();
let diff2: HashSet<_> = b.symmetric_difference(&a).collect();

assert_eq!(diff1, diff2);
assert_eq!(diff1, [1, 4].iter().collect());
```

</div>

</div>

<div id="method.intersection" class="section method">

<a href="../src/hashbrown/set.rs.html#711-721"
class="src rightside">Source</a>

#### pub fn <a href="#method.intersection" class="fn">intersection</a>\<'a\>(&'a self, other: &'a Self) -\> <a href="hash_set/struct.Intersection.html" class="struct"
title="struct hashbrown::hash_set::Intersection">Intersection</a>\<'a, T, S, A\> <a href="#" class="tooltip"
data-notable-ty="Intersection&lt;&#39;a, T, S, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Visits the values representing the intersection, i.e., the values that
are both in `self` and `other`.

##### <a href="#examples-20" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
let a: HashSet<_> = [1, 2, 3].iter().cloned().collect();
let b: HashSet<_> = [4, 2, 3, 4].iter().cloned().collect();

// Print 2, 3 in arbitrary order.
for x in a.intersection(&b) {
    println!("{}", x);
}

let intersection: HashSet<_> = a.intersection(&b).collect();
assert_eq!(intersection, [2, 3].iter().collect());
```

</div>

</div>

<div id="method.union" class="section method">

<a href="../src/hashbrown/set.rs.html#742-753"
class="src rightside">Source</a>

#### pub fn <a href="#method.union" class="fn">union</a>\<'a\>(&'a self, other: &'a Self) -\> <a href="hash_set/struct.Union.html" class="struct"
title="struct hashbrown::hash_set::Union">Union</a>\<'a, T, S, A\> <a href="#" class="tooltip"
data-notable-ty="Union&lt;&#39;a, T, S, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Visits the values representing the union, i.e., all the values in `self`
or `other`, without duplicates.

##### <a href="#examples-21" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
let a: HashSet<_> = [1, 2, 3].iter().cloned().collect();
let b: HashSet<_> = [4, 2, 3, 4].iter().cloned().collect();

// Print 1, 2, 3, 4 in arbitrary order.
for x in a.union(&b) {
    println!("{}", x);
}

let union: HashSet<_> = a.union(&b).collect();
assert_eq!(union, [1, 2, 3, 4].iter().collect());
```

</div>

</div>

<div id="method.contains" class="section method">

<a href="../src/hashbrown/set.rs.html#774-780"
class="src rightside">Source</a>

#### pub fn <a href="#method.contains" class="fn">contains</a>\<Q\>(&self, value: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\>, Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Returns `true` if the set contains a value.

The value may be any borrowed form of the set’s value type, but
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) and
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) on the borrowed
form *must* match those for the value type.

##### <a href="#examples-22" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let set: HashSet<_> = [1, 2, 3].iter().cloned().collect();
assert_eq!(set.contains(&1), true);
assert_eq!(set.contains(&4), false);
```

</div>

</div>

<div id="method.get" class="section method">

<a href="../src/hashbrown/set.rs.html#801-811"
class="src rightside">Source</a>

#### pub fn <a href="#method.get" class="fn">get</a>\<Q\>(&self, value: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\>, Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Returns a reference to the value in the set, if any, that is equal to
the given value.

The value may be any borrowed form of the set’s value type, but
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) and
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) on the borrowed
form *must* match those for the value type.

##### <a href="#examples-23" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let set: HashSet<_> = [1, 2, 3].iter().cloned().collect();
assert_eq!(set.get(&2), Some(&2));
assert_eq!(set.get(&4), None);
```

</div>

</div>

<div id="method.get_or_insert" class="section method">

<a href="../src/hashbrown/set.rs.html#828-836"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_or_insert" class="fn">get_or_insert</a>(&mut self, value: T) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="docblock">

Inserts the given `value` into the set if it is not present, then
returns a reference to the value in the set.

##### <a href="#examples-24" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut set: HashSet<_> = [1, 2, 3].iter().cloned().collect();
assert_eq!(set.len(), 3);
assert_eq!(set.get_or_insert(2), &2);
assert_eq!(set.get_or_insert(100), &100);
assert_eq!(set.len(), 4); // 100 was inserted
```

</div>

</div>

<div id="method.get_or_insert_owned" class="section method">

<a href="../src/hashbrown/set.rs.html#857-869"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_or_insert_owned" class="fn">get_or_insert_owned</a>\<Q\>(&mut self, value: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\>, Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> + <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html"
class="trait" title="trait alloc::borrow::ToOwned">ToOwned</a>\<Owned =
T\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Inserts an owned copy of the given `value` into the set if it is not
present, then returns a reference to the value in the set.

##### <a href="#examples-25" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut set: HashSet<String> = ["cat", "dog", "horse"]
    .iter().map(|&pet| pet.to_owned()).collect();

assert_eq!(set.len(), 3);
for &pet in &["cat", "dog", "fish"] {
    let value = set.get_or_insert_owned(pet);
    assert_eq!(value, pet);
}
assert_eq!(set.len(), 4); // a new "fish" was inserted
```

</div>

</div>

<div id="method.get_or_insert_with" class="section method">

<a href="../src/hashbrown/set.rs.html#890-903"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_or_insert_with" class="fn">get_or_insert_with</a>\<Q, F\>(&mut self, value: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>, f: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\>, Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnOnce.html"
class="trait" title="trait core::ops::function::FnOnce">FnOnce</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> T,

</div>

</div>

<div class="docblock">

Inserts a value computed from `f` into the set if the given `value` is
not present, then returns a reference to the value in the set.

##### <a href="#examples-26" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut set: HashSet<String> = ["cat", "dog", "horse"]
    .iter().map(|&pet| pet.to_owned()).collect();

assert_eq!(set.len(), 3);
for &pet in &["cat", "dog", "fish"] {
    let value = set.get_or_insert_with(pet, str::to_owned);
    assert_eq!(value, pet);
}
assert_eq!(set.len(), 4); // a new "fish" was inserted
```

</div>

</div>

<div id="method.entry" class="section method">

<a href="../src/hashbrown/set.rs.html#939-944"
class="src rightside">Source</a>

#### pub fn <a href="#method.entry" class="fn">entry</a>(&mut self, value: T) -\> <a href="hash_set/enum.Entry.html" class="enum"
title="enum hashbrown::hash_set::Entry">Entry</a>\<'\_, T, S, A\>

</div>

<div class="docblock">

Gets the given value’s corresponding entry in the set for in-place
manipulation.

##### <a href="#examples-27" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
use hashbrown::hash_set::Entry::*;

let mut singles = HashSet::new();
let mut dupes = HashSet::new();

for ch in "a short treatise on fungi".chars() {
    if let Vacant(dupe_entry) = dupes.entry(ch) {
        // We haven't already seen a duplicate, so
        // check if we've at least seen it once.
        match singles.entry(ch) {
            Vacant(single_entry) => {
                // We found a new character for the first time.
                single_entry.insert()
            }
            Occupied(single_entry) => {
                // We've already seen this once, "move" it to dupes.
                single_entry.remove();
                dupe_entry.insert();
            }
        }
    }
}

assert!(!singles.contains(&'t') && dupes.contains(&'t'));
assert!(singles.contains(&'u') && !dupes.contains(&'u'));
assert!(!singles.contains(&'v') && !dupes.contains(&'v'));
```

</div>

</div>

<div id="method.is_disjoint" class="section method">

<a href="../src/hashbrown/set.rs.html#963-965"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_disjoint" class="fn">is_disjoint</a>(&self, other: &Self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns `true` if `self` has no elements in common with `other`. This is
equivalent to checking for an empty intersection.

##### <a href="#examples-28" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let a: HashSet<_> = [1, 2, 3].iter().cloned().collect();
let mut b = HashSet::new();

assert_eq!(a.is_disjoint(&b), true);
b.insert(4);
assert_eq!(a.is_disjoint(&b), true);
b.insert(1);
assert_eq!(a.is_disjoint(&b), false);
```

</div>

</div>

<div id="method.is_subset" class="section method">

<a href="../src/hashbrown/set.rs.html#984-986"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_subset" class="fn">is_subset</a>(&self, other: &Self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns `true` if the set is a subset of another, i.e., `other` contains
at least all the values in `self`.

##### <a href="#examples-29" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let sup: HashSet<_> = [1, 2, 3].iter().cloned().collect();
let mut set = HashSet::new();

assert_eq!(set.is_subset(&sup), true);
set.insert(2);
assert_eq!(set.is_subset(&sup), true);
set.insert(4);
assert_eq!(set.is_subset(&sup), false);
```

</div>

</div>

<div id="method.is_superset" class="section method">

<a href="../src/hashbrown/set.rs.html#1009-1011"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_superset" class="fn">is_superset</a>(&self, other: &Self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns `true` if the set is a superset of another, i.e., `self`
contains at least all the values in `other`.

##### <a href="#examples-30" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let sub: HashSet<_> = [1, 2].iter().cloned().collect();
let mut set = HashSet::new();

assert_eq!(set.is_superset(&sub), false);

set.insert(0);
set.insert(1);
assert_eq!(set.is_superset(&sub), false);

set.insert(2);
assert_eq!(set.is_superset(&sub), true);
```

</div>

</div>

<div id="method.insert" class="section method">

<a href="../src/hashbrown/set.rs.html#1031-1033"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(&mut self, value: T) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Adds a value to the set.

If the set did not have this value present, `true` is returned.

If the set did have this value present, `false` is returned.

##### <a href="#examples-31" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut set = HashSet::new();

assert_eq!(set.insert(2), true);
assert_eq!(set.insert(2), false);
assert_eq!(set.len(), 1);
```

</div>

</div>

<div id="method.insert_unique_unchecked" class="section method">

<a href="../src/hashbrown/set.rs.html#1055-1057"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert_unique_unchecked"
class="fn">insert_unique_unchecked</a>(&mut self, value: T) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="docblock">

Insert a value the set without checking if the value already exists in
the set.

Returns a reference to the value just inserted.

This operation is safe if a value does not exist in the set.

However, if a value exists in the set already, the behavior is
unspecified: this operation may panic, loop forever, or any following
operation with the set may panic, loop forever or return arbitrary
result.

That said, this operation (and following operations) are guaranteed to
not violate memory safety.

This operation is faster than regular insert, because it does not
perform lookup before insertion.

This operation is useful during initial population of the set. For
example, when constructing a set from another set, we know that values
are unique.

</div>

<div id="method.replace" class="section method">

<a href="../src/hashbrown/set.rs.html#1075-1083"
class="src rightside">Source</a>

#### pub fn <a href="#method.replace" class="fn">replace</a>(&mut self, value: T) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div class="docblock">

Adds a value to the set, replacing the existing value, if any, that is
equal to the given one. Returns the replaced value.

##### <a href="#examples-32" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut set = HashSet::new();
set.insert(Vec::<i32>::new());

assert_eq!(set.get(&[][..]).unwrap().capacity(), 0);
set.replace(Vec::with_capacity(10));
assert_eq!(set.get(&[][..]).unwrap().capacity(), 10);
```

</div>

</div>

<div id="method.remove" class="section method">

<a href="../src/hashbrown/set.rs.html#1107-1113"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove" class="fn">remove</a>\<Q\>(&mut self, value: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\>, Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Removes a value from the set. Returns whether the value was present in
the set.

The value may be any borrowed form of the set’s value type, but
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) and
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) on the borrowed
form *must* match those for the value type.

##### <a href="#examples-33" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut set = HashSet::new();

set.insert(2);
assert_eq!(set.remove(&2), true);
assert_eq!(set.remove(&2), false);
```

</div>

</div>

<div id="method.take" class="section method">

<a href="../src/hashbrown/set.rs.html#1134-1144"
class="src rightside">Source</a>

#### pub fn <a href="#method.take" class="fn">take</a>\<Q\>(&mut self, value: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\>, Q:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Removes and returns the value in the set, if any, that is equal to the
given one.

The value may be any borrowed form of the set’s value type, but
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) and
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) on the borrowed
form *must* match those for the value type.

##### <a href="#examples-34" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let mut set: HashSet<_> = [1, 2, 3].iter().cloned().collect();
assert_eq!(set.take(&2), Some(2));
assert_eq!(set.take(&2), None);
```

</div>

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-BitAnd%3C%26HashSet%3CT,+S,+A%3E%3E-for-%26HashSet%3CT,+S,+A%3E"
class="section impl">

<a href="../src/hashbrown/set.rs.html#1319-1350"
class="src rightside">Source</a><a
href="#impl-BitAnd%3C%26HashSet%3CT,+S,+A%3E%3E-for-%26HashSet%3CT,+S,+A%3E"
class="anchor">§</a>

### impl\<T, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitAnd.html"
class="trait" title="trait core::ops::bit::BitAnd">BitAnd</a>\<&<a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>\> for &<a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>, A:
Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.bitand" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#1347-1349"
class="src rightside">Source</a><a href="#method.bitand" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitAnd.html#tymethod.bitand"
class="fn">bitand</a>(self, rhs: &<a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>) -\> <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>

</div>

<div class="docblock">

Returns the intersection of `self` and `rhs` as a new `HashSet<T, S>`.

##### <a href="#examples-36" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let a: HashSet<_> = vec![1, 2, 3].into_iter().collect();
let b: HashSet<_> = vec![2, 3, 4].into_iter().collect();

let set = &a & &b;

let mut i = 0;
let expected = [2, 3];
for x in &set {
    assert!(expected.contains(x));
    i += 1;
}
assert_eq!(i, expected.len());
```

</div>

</div>

<div id="associatedtype.Output-1"
class="section associatedtype trait-impl">

<a href="../src/hashbrown/set.rs.html#1325"
class="src rightside">Source</a><a href="#associatedtype.Output-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitAnd.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>

</div>

<div class="docblock">

The resulting type after applying the `&` operator.

</div>

</div>

<div id="impl-BitOr%3C%26HashSet%3CT,+S,+A%3E%3E-for-%26HashSet%3CT,+S,+A%3E"
class="section impl">

<a href="../src/hashbrown/set.rs.html#1286-1317"
class="src rightside">Source</a><a
href="#impl-BitOr%3C%26HashSet%3CT,+S,+A%3E%3E-for-%26HashSet%3CT,+S,+A%3E"
class="anchor">§</a>

### impl\<T, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitOr.html"
class="trait" title="trait core::ops::bit::BitOr">BitOr</a>\<&<a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>\> for &<a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>, A:
Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.bitor" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#1314-1316"
class="src rightside">Source</a><a href="#method.bitor" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitOr.html#tymethod.bitor"
class="fn">bitor</a>(self, rhs: &<a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>) -\> <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>

</div>

<div class="docblock">

Returns the union of `self` and `rhs` as a new `HashSet<T, S>`.

##### <a href="#examples-35" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let a: HashSet<_> = vec![1, 2, 3].into_iter().collect();
let b: HashSet<_> = vec![3, 4, 5].into_iter().collect();

let set = &a | &b;

let mut i = 0;
let expected = [1, 2, 3, 4, 5];
for x in &set {
    assert!(expected.contains(x));
    i += 1;
}
assert_eq!(i, expected.len());
```

</div>

</div>

<div id="associatedtype.Output"
class="section associatedtype trait-impl">

<a href="../src/hashbrown/set.rs.html#1292"
class="src rightside">Source</a><a href="#associatedtype.Output" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitOr.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>

</div>

<div class="docblock">

The resulting type after applying the `|` operator.

</div>

</div>

<div id="impl-BitXor%3C%26HashSet%3CT,+S%3E%3E-for-%26HashSet%3CT,+S%3E"
class="section impl">

<a href="../src/hashbrown/set.rs.html#1352-1382"
class="src rightside">Source</a><a
href="#impl-BitXor%3C%26HashSet%3CT,+S%3E%3E-for-%26HashSet%3CT,+S%3E"
class="anchor">§</a>

### impl\<T, S\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitXor.html"
class="trait" title="trait core::ops::bit::BitXor">BitXor</a>\<&<a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>\> for &<a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>,

</div>

</div>

<div class="impl-items">

<div id="method.bitxor" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#1379-1381"
class="src rightside">Source</a><a href="#method.bitxor" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitXor.html#tymethod.bitxor"
class="fn">bitxor</a>(self, rhs: &<a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>) -\> <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>

</div>

<div class="docblock">

Returns the symmetric difference of `self` and `rhs` as a new
`HashSet<T, S>`.

##### <a href="#examples-37" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let a: HashSet<_> = vec![1, 2, 3].into_iter().collect();
let b: HashSet<_> = vec![3, 4, 5].into_iter().collect();

let set = &a ^ &b;

let mut i = 0;
let expected = [1, 2, 4, 5];
for x in &set {
    assert!(expected.contains(x));
    i += 1;
}
assert_eq!(i, expected.len());
```

</div>

</div>

<div id="associatedtype.Output-2"
class="section associatedtype trait-impl">

<a href="../src/hashbrown/set.rs.html#1357"
class="src rightside">Source</a><a href="#associatedtype.Output-2" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/bit/trait.BitXor.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>

</div>

<div class="docblock">

The resulting type after applying the `^` operator.

</div>

</div>

<div id="impl-Clone-for-HashSet%3CT,+S,+A%3E" class="section impl">

<a href="../src/hashbrown/set.rs.html#119-129"
class="src rightside">Source</a><a href="#impl-Clone-for-HashSet%3CT,+S,+A%3E" class="anchor">§</a>

### impl\<T: <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, S: <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#120-124"
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

<a href="../src/hashbrown/set.rs.html#126-128"
class="src rightside">Source</a><a href="#method.clone_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from"
class="fn">clone_from</a>(&mut self, source: &Self)

</div>

<div class="docblock">

Performs copy-assignment from `source`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from)

</div>

</div>

<div id="impl-Debug-for-HashSet%3CT,+S,+A%3E" class="section impl">

<a href="../src/hashbrown/set.rs.html#1170-1178"
class="src rightside">Source</a><a href="#impl-Debug-for-HashSet%3CT,+S,+A%3E" class="anchor">§</a>

### impl\<T, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, A: Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#1175-1177"
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

<div id="impl-Default-for-HashSet%3CT,+S,+A%3E" class="section impl">

<a href="../src/hashbrown/set.rs.html#1272-1284"
class="src rightside">Source</a><a href="#impl-Default-for-HashSet%3CT,+S,+A%3E" class="anchor">§</a>

### impl\<T, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where S: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>, A: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a> +
Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.default" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#1279-1283"
class="src rightside">Source</a><a href="#method.default" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html#tymethod.default"
class="fn">default</a>() -\> Self

</div>

<div class="docblock">

Creates an empty `HashSet<T, S>` with the `Default` value for the
hasher.

</div>

</div>

<div id="impl-Extend%3C%26T%3E-for-HashSet%3CT,+S,+A%3E"
class="section impl">

<a href="../src/hashbrown/set.rs.html#1248-1270"
class="src rightside">Source</a><a href="#impl-Extend%3C%26T%3E-for-HashSet%3CT,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, T, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a T</a>\> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where T: 'a +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>, A:
Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.extend-1" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#1255-1257"
class="src rightside">Source</a><a href="#method.extend-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a T</a>\>\>(&mut self, iter: I)

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
class="fn">extend_reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
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

<div id="impl-Extend%3CT%3E-for-HashSet%3CT,+S,+A%3E"
class="section impl">

<a href="../src/hashbrown/set.rs.html#1224-1246"
class="src rightside">Source</a><a href="#impl-Extend%3CT%3E-for-HashSet%3CT,+S,+A%3E"
class="anchor">§</a>

### impl\<T, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<T\> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>, A:
Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.extend" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#1231-1233"
class="src rightside">Source</a><a href="#method.extend" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = T\>\>(&mut self, iter: I)

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
class="fn">extend_reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
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

<div id="impl-From%3CHashMap%3CT,+(),+S,+A%3E%3E-for-HashSet%3CT,+S,+A%3E"
class="section impl">

<a href="../src/hashbrown/set.rs.html#1180-1187"
class="src rightside">Source</a><a
href="#impl-From%3CHashMap%3CT,+(),+S,+A%3E%3E-for-HashSet%3CT,+S,+A%3E"
class="anchor">§</a>

### impl\<T, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<T, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.unit.html"
class="primitive">()</a>, S, A\>\> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where A: Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#1184-1186"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(map: <a href="struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<T, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.unit.html"
class="primitive">()</a>, S, A\>) -\> Self

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-FromIterator%3CT%3E-for-HashSet%3CT,+S,+A%3E"
class="section impl">

<a href="../src/hashbrown/set.rs.html#1189-1201"
class="src rightside">Source</a><a href="#impl-FromIterator%3CT%3E-for-HashSet%3CT,+S,+A%3E"
class="anchor">§</a>

### impl\<T, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html"
class="trait"
title="trait core::iter::traits::collect::FromIterator">FromIterator</a>\<T\> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>, A: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a> +
Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.from_iter" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#1196-1200"
class="src rightside">Source</a><a href="#method.from_iter" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html#tymethod.from_iter"
class="fn">from_iter</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = T\>\>(iter: I) -\> Self

</div>

<div class="docblock">

Creates a value from an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html#tymethod.from_iter)

</div>

</div>

<div id="impl-IntoIterator-for-%26HashSet%3CT,+S,+A%3E"
class="section impl">

<a href="../src/hashbrown/set.rs.html#1514-1522"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-%26HashSet%3CT,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, T, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for &'a <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

</div>

<div class="impl-items">

<div id="associatedtype.Item" class="section associatedtype trait-impl">

<a href="../src/hashbrown/set.rs.html#1515"
class="src rightside">Source</a><a href="#associatedtype.Item" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a T</a>

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter"
class="section associatedtype trait-impl">

<a href="../src/hashbrown/set.rs.html#1516"
class="src rightside">Source</a><a href="#associatedtype.IntoIter" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="hash_set/struct.Iter.html" class="struct"
title="struct hashbrown::hash_set::Iter">Iter</a>\<'a, T\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

<div id="method.into_iter" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#1519-1521"
class="src rightside">Source</a><a href="#method.into_iter" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter"
class="fn">into_iter</a>(self) -\> <a href="hash_set/struct.Iter.html" class="struct"
title="struct hashbrown::hash_set::Iter">Iter</a>\<'a, T\> <a href="#" class="tooltip"
data-notable-ty="Iter&lt;&#39;a, T&gt;">ⓘ</a>

</div>

<div class="docblock">

Creates an iterator from a value. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter)

</div>

</div>

<div id="impl-IntoIterator-for-HashSet%3CT,+S,+A%3E"
class="section impl">

<a href="../src/hashbrown/set.rs.html#1524-1554"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-HashSet%3CT,+S,+A%3E"
class="anchor">§</a>

### impl\<T, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

</div>

<div class="impl-items">

<div id="method.into_iter-1" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#1549-1553"
class="src rightside">Source</a><a href="#method.into_iter-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter"
class="fn">into_iter</a>(self) -\> <a href="hash_set/struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_set::IntoIter">IntoIter</a>\<T, A\> <a href="#" class="tooltip" data-notable-ty="IntoIter&lt;T, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Creates a consuming iterator, that is, one that moves each value out of
the set in arbitrary order. The set cannot be used after calling this.

##### <a href="#examples-39" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;
let mut set = HashSet::new();
set.insert("a".to_string());
set.insert("b".to_string());

// Not possible to collect to a Vec<String> with a regular `.iter()`.
let v: Vec<String> = set.into_iter().collect();

// Will print in an arbitrary order.
for x in &v {
    println!("{}", x);
}
```

</div>

</div>

<div id="associatedtype.Item-1"
class="section associatedtype trait-impl">

<a href="../src/hashbrown/set.rs.html#1525"
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

<a href="../src/hashbrown/set.rs.html#1526"
class="src rightside">Source</a><a href="#associatedtype.IntoIter-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="hash_set/struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_set::IntoIter">IntoIter</a>\<T, A\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

</div>

<div id="impl-PartialEq-for-HashSet%3CT,+S,+A%3E" class="section impl">

<a href="../src/hashbrown/set.rs.html#1147-1160"
class="src rightside">Source</a><a href="#impl-PartialEq-for-HashSet%3CT,+S,+A%3E" class="anchor">§</a>

### impl\<T, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>, A:
Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#1153-1159"
class="src rightside">Source</a><a href="#method.eq" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#tymethod.eq"
class="fn">eq</a>(&self, other: &Self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
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
class="fn">ne</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `!=`. The default implementation is almost always sufficient,
and should not be overridden without very good reason.

</div>

</div>

<div id="impl-Sub%3C%26HashSet%3CT,+S%3E%3E-for-%26HashSet%3CT,+S%3E"
class="section impl">

<a href="../src/hashbrown/set.rs.html#1384-1414"
class="src rightside">Source</a><a href="#impl-Sub%3C%26HashSet%3CT,+S%3E%3E-for-%26HashSet%3CT,+S%3E"
class="anchor">§</a>

### impl\<T, S\> <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Sub.html"
class="trait" title="trait core::ops::arith::Sub">Sub</a>\<&<a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>\> for &<a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>,

</div>

</div>

<div class="impl-items">

<div id="method.sub" class="section method trait-impl">

<a href="../src/hashbrown/set.rs.html#1411-1413"
class="src rightside">Source</a><a href="#method.sub" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Sub.html#tymethod.sub"
class="fn">sub</a>(self, rhs: &<a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>) -\> <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>

</div>

<div class="docblock">

Returns the difference of `self` and `rhs` as a new `HashSet<T, S>`.

##### <a href="#examples-38" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashSet;

let a: HashSet<_> = vec![1, 2, 3].into_iter().collect();
let b: HashSet<_> = vec![3, 4, 5].into_iter().collect();

let set = &a - &b;

let mut i = 0;
let expected = [1, 2];
for x in &set {
    assert!(expected.contains(x));
    i += 1;
}
assert_eq!(i, expected.len());
```

</div>

</div>

<div id="associatedtype.Output-3"
class="section associatedtype trait-impl">

<a href="../src/hashbrown/set.rs.html#1389"
class="src rightside">Source</a><a href="#associatedtype.Output-3" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Sub.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S\>

</div>

<div class="docblock">

The resulting type after applying the `-` operator.

</div>

</div>

<div id="impl-Eq-for-HashSet%3CT,+S,+A%3E" class="section impl">

<a href="../src/hashbrown/set.rs.html#1162-1168"
class="src rightside">Source</a><a href="#impl-Eq-for-HashSet%3CT,+S,+A%3E" class="anchor">§</a>

### impl\<T, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>, A:
Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-HashSet%3CT,+S,+A%3E" class="section impl">

<a href="#impl-Freeze-for-HashSet%3CT,+S,+A%3E" class="anchor">§</a>

### impl\<T, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>,

</div>

</div>

<div id="impl-RefUnwindSafe-for-HashSet%3CT,+S,+A%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-HashSet%3CT,+S,+A%3E"
class="anchor">§</a>

### impl\<T, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where S: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
A: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
T: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

<div id="impl-Send-for-HashSet%3CT,+S,+A%3E" class="section impl">

<a href="#impl-Send-for-HashSet%3CT,+S,+A%3E" class="anchor">§</a>

### impl\<T, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-HashSet%3CT,+S,+A%3E" class="section impl">

<a href="#impl-Sync-for-HashSet%3CT,+S,+A%3E" class="anchor">§</a>

### impl\<T, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>,

</div>

</div>

<div id="impl-Unpin-for-HashSet%3CT,+S,+A%3E" class="section impl">

<a href="#impl-Unpin-for-HashSet%3CT,+S,+A%3E" class="anchor">§</a>

### impl\<T, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-HashSet%3CT,+S,+A%3E" class="section impl">

<a href="#impl-UnwindSafe-for-HashSet%3CT,+S,+A%3E" class="anchor">§</a>

### impl\<T, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where S: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a>, A: <a
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
class="fn">borrow</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
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
class="fn">borrow_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
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
class="fn">clone_to_uninit</a>(&self, dest: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.pointer.html"
class="primitive">*mut</a> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u8.html"
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
class="fn">clone_into</a>(&self, target: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
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
