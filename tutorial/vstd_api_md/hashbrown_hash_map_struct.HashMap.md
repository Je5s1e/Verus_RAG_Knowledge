<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[hashbrown](../index.html)::[hash_map](index.html)

</div>

# Struct <span class="struct">HashMap</span> Copy item path

<span class="sub-heading"><a href="../../src/hashbrown/map.rs.html#188-191" class="src">Source</a>
</span>

</div>

``` rust
pub struct HashMap<K, V, S = DefaultHashBuilder, A: Allocator + Clone = Global> { /* private fields */ }
```

Expand description

<div class="docblock">

A hash map implemented with quadratic probing and SIMD lookup.

The default hashing algorithm is currently
[`AHash`](https://crates.io/crates/ahash), though this is subject to
change at any point in the future. This hash function is very fast for
all types of keys, but this algorithm will typically *not* protect
against attacks such as HashDoS.

The hashing algorithm can be replaced on a per-`HashMap` basis using the
[`default`](#method.default), [`with_hasher`](#method.with_hasher), and
[`with_capacity_and_hasher`](#method.with_capacity_and_hasher) methods.
Many alternative algorithms are available on crates.io, such as the
[`fnv`](https://crates.io/crates/fnv) crate.

It is required that the keys implement the
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) and
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) traits,
although this can frequently be achieved by using
`#[derive(PartialEq, Eq, Hash)]`. If you implement these yourself, it is
important that the following property holds:

<div class="example-wrap">

``` text
k1 == k2 -> hash(k1) == hash(k2)
```

</div>

In other words, if two keys are equal, their hashes must be equal.

It is a logic error for a key to be modified in such a way that the
key’s hash, as determined by the
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) trait, or
its equality, as determined by the
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) trait, changes
while it is in the map. This is normally only possible through
[`Cell`](https://doc.rust-lang.org/std/cell/struct.Cell.html),
[`RefCell`](https://doc.rust-lang.org/std/cell/struct.RefCell.html),
global state, I/O, or unsafe code.

It is also a logic error for the
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html)
implementation of a key to panic. This is generally only possible if the
trait is implemented manually. If a panic does occur then the contents
of the `HashMap` may become corrupted and some items may be dropped from
the table.

## <a href="#examples" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

// Type inference lets us omit an explicit type signature (which
// would be `HashMap<String, String>` in this example).
let mut book_reviews = HashMap::new();

// Review some books.
book_reviews.insert(
    "Adventures of Huckleberry Finn".to_string(),
    "My favorite book.".to_string(),
);
book_reviews.insert(
    "Grimms' Fairy Tales".to_string(),
    "Masterpiece.".to_string(),
);
book_reviews.insert(
    "Pride and Prejudice".to_string(),
    "Very enjoyable.".to_string(),
);
book_reviews.insert(
    "The Adventures of Sherlock Holmes".to_string(),
    "Eye lyked it alot.".to_string(),
);

// Check for a specific one.
// When collections store owned values (String), they can still be
// queried using references (&str).
if !book_reviews.contains_key("Les Misérables") {
    println!("We've got {} reviews, but Les Misérables ain't one.",
             book_reviews.len());
}

// oops, this review has a lot of spelling mistakes, let's delete it.
book_reviews.remove("The Adventures of Sherlock Holmes");

// Look up the values associated with some keys.
let to_find = ["Pride and Prejudice", "Alice's Adventure in Wonderland"];
for &book in &to_find {
    match book_reviews.get(book) {
        Some(review) => println!("{}: {}", book, review),
        None => println!("{} is unreviewed.", book)
    }
}

// Look up the value for a key (will panic if the key is not found).
println!("Review for Jane: {}", book_reviews["Pride and Prejudice"]);

// Iterate over everything.
for (book, review) in &book_reviews {
    println!("{}: \"{}\"", book, review);
}
```

</div>

`HashMap` also implements an [`Entry API`](#method.entry), which allows
for more complex methods of getting, setting, updating and removing keys
and their values:

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

// type inference lets us omit an explicit type signature (which
// would be `HashMap<&str, u8>` in this example).
let mut player_stats = HashMap::new();

fn random_stat_buff() -> u8 {
    // could actually return some random value here - let's just return
    // some fixed value for now
    42
}

// insert a key only if it doesn't already exist
player_stats.entry("health").or_insert(100);

// insert a key using a function that provides a new value only if it
// doesn't already exist
player_stats.entry("defence").or_insert_with(random_stat_buff);

// update a key, guarding against the key possibly not being set
let stat = player_stats.entry("attack").or_insert(100);
*stat += random_stat_buff();
```

</div>

The easiest way to use `HashMap` with a custom key type is to derive
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) and
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html). We must
also derive
[`PartialEq`](https://doc.rust-lang.org/std/cmp/trait.PartialEq.html).

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

#[derive(Hash, Eq, PartialEq, Debug)]
struct Viking {
    name: String,
    country: String,
}

impl Viking {
    /// Creates a new Viking.
    fn new(name: &str, country: &str) -> Viking {
        Viking { name: name.to_string(), country: country.to_string() }
    }
}

// Use a HashMap to store the vikings' health points.
let mut vikings = HashMap::new();

vikings.insert(Viking::new("Einar", "Norway"), 25);
vikings.insert(Viking::new("Olaf", "Denmark"), 24);
vikings.insert(Viking::new("Harald", "Iceland"), 12);

// Use derived implementation to print the status of the vikings.
for (viking, health) in &vikings {
    println!("{:?} has {} hp", viking, health);
}
```

</div>

A `HashMap` with fixed list of elements can be initialized from an
array:

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let timber_resources: HashMap<&str, i32> = [("Norway", 100), ("Denmark", 50), ("Iceland", 10)]
    .iter().cloned().collect();
// use the values stored in map
```

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-HashMap%3CK,+V,+S%3E" class="section impl">

<a href="../../src/hashbrown/map.rs.html#351-425"
class="src rightside">Source</a><a href="#impl-HashMap%3CK,+V,+S%3E" class="anchor">§</a>

### impl\<K, V, S\> <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S\>

</div>

<div class="impl-items">

<div id="method.with_hasher" class="section method">

<a href="../../src/hashbrown/map.rs.html#382-387"
class="src rightside">Source</a>

#### pub const fn <a href="#method.with_hasher" class="fn">with_hasher</a>(hash_builder: S) -\> Self

</div>

<div class="docblock">

Creates an empty `HashMap` which will use the given hash builder to hash
keys.

The hash map is initially created with a capacity of 0, so it will not
allocate until it is first inserted into.

Warning: `hash_builder` is normally randomly generated, and is designed
to allow HashMaps to be resistant to attacks that cause many collisions
and very poor performance. Setting it manually using this function can
expose a DoS attack vector.

The `hash_builder` passed should implement the
[`BuildHasher`](https://doc.rust-lang.org/std/hash/trait.BuildHasher.html)
trait for the HashMap to be useful, see its documentation for details.

##### <a href="#examples-1" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::DefaultHashBuilder;

let s = DefaultHashBuilder::default();
let mut map = HashMap::with_hasher(s);
assert_eq!(map.len(), 0);
assert_eq!(map.capacity(), 0);

map.insert(1, 2);
```

</div>

</div>

<div id="method.with_capacity_and_hasher" class="section method">

<a href="../../src/hashbrown/map.rs.html#419-424"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_capacity_and_hasher"
class="fn">with_capacity_and_hasher</a>(capacity: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>, hash_builder: S) -\> Self

</div>

<div class="docblock">

Creates an empty `HashMap` with the specified capacity, using
`hash_builder` to hash the keys.

The hash map will be able to hold at least `capacity` elements without
reallocating. If `capacity` is 0, the hash map will not allocate.

Warning: `hash_builder` is normally randomly generated, and is designed
to allow HashMaps to be resistant to attacks that cause many collisions
and very poor performance. Setting it manually using this function can
expose a DoS attack vector.

The `hash_builder` passed should implement the
[`BuildHasher`](https://doc.rust-lang.org/std/hash/trait.BuildHasher.html)
trait for the HashMap to be useful, see its documentation for details.

##### <a href="#examples-2" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::DefaultHashBuilder;

let s = DefaultHashBuilder::default();
let mut map = HashMap::with_capacity_and_hasher(10, s);
assert_eq!(map.len(), 0);
assert!(map.capacity() >= 10);

map.insert(1, 2);
```

</div>

</div>

</div>

<div id="impl-HashMap%3CK,+V,+S,+A%3E" class="section impl">

<a href="../../src/hashbrown/map.rs.html#427-981"
class="src rightside">Source</a><a href="#impl-HashMap%3CK,+V,+S,+A%3E" class="anchor">§</a>

### impl\<K, V, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.allocator" class="section method">

<a href="../../src/hashbrown/map.rs.html#430-432"
class="src rightside">Source</a>

#### pub fn <a href="#method.allocator" class="fn">allocator</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;A</a>

</div>

<div class="docblock">

Returns a reference to the underlying allocator.

</div>

<div id="method.with_hasher_in" class="section method">

<a href="../../src/hashbrown/map.rs.html#455-460"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_hasher_in" class="fn">with_hasher_in</a>(hash_builder: S, alloc: A) -\> Self

</div>

<div class="docblock">

Creates an empty `HashMap` which will use the given hash builder to hash
keys. It will be allocated with the given allocator.

The created map has the default initial capacity.

Warning: `hash_builder` is normally randomly generated, and is designed
to allow HashMaps to be resistant to attacks that cause many collisions
and very poor performance. Setting it manually using this function can
expose a DoS attack vector.

##### <a href="#examples-3" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::DefaultHashBuilder;

let s = DefaultHashBuilder::default();
let mut map = HashMap::with_hasher(s);
map.insert(1, 2);
```

</div>

</div>

<div id="method.with_capacity_and_hasher_in" class="section method">

<a href="../../src/hashbrown/map.rs.html#484-489"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_capacity_and_hasher_in"
class="fn">with_capacity_and_hasher_in</a>( capacity: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>, hash_builder: S, alloc: A, ) -\> Self

</div>

<div class="docblock">

Creates an empty `HashMap` with the specified capacity, using
`hash_builder` to hash the keys. It will be allocated with the given
allocator.

The hash map will be able to hold at least `capacity` elements without
reallocating. If `capacity` is 0, the hash map will not allocate.

Warning: `hash_builder` is normally randomly generated, and is designed
to allow HashMaps to be resistant to attacks that cause many collisions
and very poor performance. Setting it manually using this function can
expose a DoS attack vector.

##### <a href="#examples-4" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::DefaultHashBuilder;

let s = DefaultHashBuilder::default();
let mut map = HashMap::with_capacity_and_hasher(10, s);
map.insert(1, 2);
```

</div>

</div>

<div id="method.hasher" class="section method">

<a href="../../src/hashbrown/map.rs.html#506-508"
class="src rightside">Source</a>

#### pub fn <a href="#method.hasher" class="fn">hasher</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;S</a>

</div>

<div class="docblock">

Returns a reference to the map’s
[`BuildHasher`](https://doc.rust-lang.org/std/hash/trait.BuildHasher.html).

##### <a href="#examples-5" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::DefaultHashBuilder;

let hasher = DefaultHashBuilder::default();
let map: HashMap<i32, i32> = HashMap::with_hasher(hasher);
let hasher: &DefaultHashBuilder = map.hasher();
```

</div>

</div>

<div id="method.capacity" class="section method">

<a href="../../src/hashbrown/map.rs.html#524-526"
class="src rightside">Source</a>

#### pub fn <a href="#method.capacity" class="fn">capacity</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Returns the number of elements the map can hold without reallocating.

This number is a lower bound; the `HashMap<K, V>` might be able to hold
more, but is guaranteed to be able to hold at least this many.

##### <a href="#examples-6" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
let map: HashMap<i32, i32> = HashMap::with_capacity(100);
assert_eq!(map.len(), 0);
assert!(map.capacity() >= 100);
```

</div>

</div>

<div id="method.keys" class="section method">

<a href="../../src/hashbrown/map.rs.html#556-558"
class="src rightside">Source</a>

#### pub fn <a href="#method.keys" class="fn">keys</a>(&self) -\> <a href="struct.Keys.html" class="struct"
title="struct hashbrown::hash_map::Keys">Keys</a>\<'\_, K, V\> <a href="#" class="tooltip"
data-notable-ty="Keys&lt;&#39;_, K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

An iterator visiting all keys in arbitrary order. The iterator element
type is `&'a K`.

##### <a href="#examples-7" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);
assert_eq!(map.len(), 3);
let mut vec: Vec<&str> = Vec::new();

for key in map.keys() {
    println!("{}", key);
    vec.push(*key);
}

// The `Keys` iterator produces keys in arbitrary order, so the
// keys must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, ["a", "b", "c"]);

assert_eq!(map.len(), 3);
```

</div>

</div>

<div id="method.values" class="section method">

<a href="../../src/hashbrown/map.rs.html#588-590"
class="src rightside">Source</a>

#### pub fn <a href="#method.values" class="fn">values</a>(&self) -\> <a href="struct.Values.html" class="struct"
title="struct hashbrown::hash_map::Values">Values</a>\<'\_, K, V\> <a href="#" class="tooltip"
data-notable-ty="Values&lt;&#39;_, K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

An iterator visiting all values in arbitrary order. The iterator element
type is `&'a V`.

##### <a href="#examples-8" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);
assert_eq!(map.len(), 3);
let mut vec: Vec<i32> = Vec::new();

for val in map.values() {
    println!("{}", val);
    vec.push(*val);
}

// The `Values` iterator produces values in arbitrary order, so the
// values must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, [1, 2, 3]);

assert_eq!(map.len(), 3);
```

</div>

</div>

<div id="method.values_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#626-630"
class="src rightside">Source</a>

#### pub fn <a href="#method.values_mut" class="fn">values_mut</a>(&mut self) -\> <a href="struct.ValuesMut.html" class="struct"
title="struct hashbrown::hash_map::ValuesMut">ValuesMut</a>\<'\_, K, V\> <a href="#" class="tooltip"
data-notable-ty="ValuesMut&lt;&#39;_, K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

An iterator visiting all values mutably in arbitrary order. The iterator
element type is `&'a mut V`.

##### <a href="#examples-9" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();

map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);

for val in map.values_mut() {
    *val = *val + 10;
}

assert_eq!(map.len(), 3);
let mut vec: Vec<i32> = Vec::new();

for val in map.values() {
    println!("{}", val);
    vec.push(*val);
}

// The `Values` iterator produces values in arbitrary order, so the
// values must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, [11, 12, 13]);

assert_eq!(map.len(), 3);
```

</div>

</div>

<div id="method.iter" class="section method">

<a href="../../src/hashbrown/map.rs.html#660-668"
class="src rightside">Source</a>

#### pub fn <a href="#method.iter" class="fn">iter</a>(&self) -\> <a href="struct.Iter.html" class="struct"
title="struct hashbrown::hash_map::Iter">Iter</a>\<'\_, K, V\> <a href="#" class="tooltip"
data-notable-ty="Iter&lt;&#39;_, K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

An iterator visiting all key-value pairs in arbitrary order. The
iterator element type is `(&'a K, &'a V)`.

##### <a href="#examples-10" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);
assert_eq!(map.len(), 3);
let mut vec: Vec<(&str, i32)> = Vec::new();

for (key, val) in map.iter() {
    println!("key: {} val: {}", key, val);
    vec.push((*key, *val));
}

// The `Iter` iterator produces items in arbitrary order, so the
// items must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, [("a", 1), ("b", 2), ("c", 3)]);

assert_eq!(map.len(), 3);
```

</div>

</div>

<div id="method.iter_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#705-713"
class="src rightside">Source</a>

#### pub fn <a href="#method.iter_mut" class="fn">iter_mut</a>(&mut self) -\> <a href="struct.IterMut.html" class="struct"
title="struct hashbrown::hash_map::IterMut">IterMut</a>\<'\_, K, V\> <a href="#" class="tooltip"
data-notable-ty="IterMut&lt;&#39;_, K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

An iterator visiting all key-value pairs in arbitrary order, with
mutable references to the values. The iterator element type is
`(&'a K, &'a mut V)`.

##### <a href="#examples-11" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);

// Update all values
for (_, val) in map.iter_mut() {
    *val *= 2;
}

assert_eq!(map.len(), 3);
let mut vec: Vec<(&str, i32)> = Vec::new();

for (key, val) in &map {
    println!("key: {} val: {}", key, val);
    vec.push((*key, *val));
}

// The `Iter` iterator produces items in arbitrary order, so the
// items must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, [("a", 2), ("b", 4), ("c", 6)]);

assert_eq!(map.len(), 3);
```

</div>

</div>

<div id="method.len" class="section method">

<a href="../../src/hashbrown/map.rs.html#734-736"
class="src rightside">Source</a>

#### pub fn <a href="#method.len" class="fn">len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Returns the number of elements in the map.

##### <a href="#examples-12" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut a = HashMap::new();
assert_eq!(a.len(), 0);
a.insert(1, "a");
assert_eq!(a.len(), 1);
```

</div>

</div>

<div id="method.is_empty" class="section method">

<a href="../../src/hashbrown/map.rs.html#751-753"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_empty" class="fn">is_empty</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns `true` if the map contains no elements.

##### <a href="#examples-13" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut a = HashMap::new();
assert!(a.is_empty());
a.insert(1, "a");
assert!(!a.is_empty());
```

</div>

</div>

<div id="method.drain" class="section method">

<a href="../../src/hashbrown/map.rs.html#794-798"
class="src rightside">Source</a>

#### pub fn <a href="#method.drain" class="fn">drain</a>(&mut self) -\> <a href="struct.Drain.html" class="struct"
title="struct hashbrown::hash_map::Drain">Drain</a>\<'\_, K, V, A\> <a href="#" class="tooltip"
data-notable-ty="Drain&lt;&#39;_, K, V, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Clears the map, returning all key-value pairs as an iterator. Keeps the
allocated memory for reuse.

If the returned iterator is dropped before being fully consumed, it
drops the remaining key-value pairs. The returned iterator keeps a
mutable borrow on the vector to optimize its implementation.

##### <a href="#examples-14" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut a = HashMap::new();
a.insert(1, "a");
a.insert(2, "b");
let capacity_before_drain = a.capacity();

for (k, v) in a.drain().take(1) {
    assert!(k == 1 || k == 2);
    assert!(v == "a" || v == "b");
}

// As we can see, the map is empty and contains no element.
assert!(a.is_empty() && a.len() == 0);
// But map capacity is equal to old one.
assert_eq!(a.capacity(), capacity_before_drain);

let mut a = HashMap::new();
a.insert(1, "a");
a.insert(2, "b");

{   // Iterator is dropped without being consumed.
    let d = a.drain();
}

// But the map is empty even if we do not use Drain iterator.
assert!(a.is_empty());
```

</div>

</div>

<div id="method.retain" class="section method">

<a href="../../src/hashbrown/map.rs.html#826-839"
class="src rightside">Source</a>

#### pub fn <a href="#method.retain" class="fn">retain</a>\<F\>(&mut self, f: F)

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;K</a>,
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Retains only the elements specified by the predicate. Keeps the
allocated memory for reuse.

In other words, remove all pairs `(k, v)` such that `f(&k, &mut v)`
returns `false`. The elements are visited in unsorted (and unspecified)
order.

##### <a href="#examples-15" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<i32, i32> = (0..8).map(|x|(x, x*10)).collect();
assert_eq!(map.len(), 8);
let capacity_before_retain = map.capacity();

map.retain(|&k, _| k % 2 == 0);

// We can see, that the number of elements inside map is changed.
assert_eq!(map.len(), 4);
// But map capacity is equal to old one.
assert_eq!(map.capacity(), capacity_before_retain);

let mut vec: Vec<(i32, i32)> = map.iter().map(|(&k, &v)| (k, v)).collect();
vec.sort_unstable();
assert_eq!(vec, [(0, 0), (2, 20), (4, 40), (6, 60)]);
```

</div>

</div>

<div id="method.drain_filter" class="section method">

<a href="../../src/hashbrown/map.rs.html#889-900"
class="src rightside">Source</a>

#### pub fn <a href="#method.drain_filter" class="fn">drain_filter</a>\<F\>(&mut self, f: F) -\> <a href="struct.DrainFilter.html" class="struct"
title="struct hashbrown::hash_map::DrainFilter">DrainFilter</a>\<'\_, K, V, F, A\> <a href="#" class="tooltip"
data-notable-ty="DrainFilter&lt;&#39;_, K, V, F, A&gt;">ⓘ</a>

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;K</a>,
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>) -\>
<a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>,

</div>

</div>

<div class="docblock">

Drains elements which are true under the given predicate, and returns an
iterator over the removed items.

In other words, move all pairs `(k, v)` such that `f(&k, &mut v)`
returns `true` out into another iterator.

Note that `drain_filter` lets you mutate every value in the filter
closure, regardless of whether you choose to keep or remove it.

When the returned DrainedFilter is dropped, any remaining elements that
satisfy the predicate are dropped from the table.

It is unspecified how many more elements will be subjected to the
closure if a panic occurs in the closure, or a panic occurs while
dropping an element, or if the `DrainFilter` value is leaked.

Keeps the allocated memory for reuse.

##### <a href="#examples-16" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<i32, i32> = (0..8).map(|x| (x, x)).collect();
let capacity_before_drain_filter = map.capacity();
let drained: HashMap<i32, i32> = map.drain_filter(|k, _v| k % 2 == 0).collect();

let mut evens = drained.keys().cloned().collect::<Vec<_>>();
let mut odds = map.keys().cloned().collect::<Vec<_>>();
evens.sort();
odds.sort();

assert_eq!(evens, vec![0, 2, 4, 6]);
assert_eq!(odds, vec![1, 3, 5, 7]);
// Map capacity is equal to old one.
assert_eq!(map.capacity(), capacity_before_drain_filter);

let mut map: HashMap<i32, i32> = (0..8).map(|x| (x, x)).collect();

{   // Iterator is dropped without being consumed.
    let d = map.drain_filter(|k, _v| k % 2 != 0);
}

// But the map lens have been reduced by half
// even if we do not use DrainFilter iterator.
assert_eq!(map.len(), 4);
```

</div>

</div>

<div id="method.clear" class="section method">

<a href="../../src/hashbrown/map.rs.html#922-924"
class="src rightside">Source</a>

#### pub fn <a href="#method.clear" class="fn">clear</a>(&mut self)

</div>

<div class="docblock">

Clears the map, removing all key-value pairs. Keeps the allocated memory
for reuse.

##### <a href="#examples-17" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut a = HashMap::new();
a.insert(1, "a");
let capacity_before_clear = a.capacity();

a.clear();

// Map is empty.
assert!(a.is_empty());
// But map capacity is equal to old one.
assert_eq!(a.capacity(), capacity_before_clear);
```

</div>

</div>

<div id="method.into_keys" class="section method">

<a href="../../src/hashbrown/map.rs.html#948-952"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_keys" class="fn">into_keys</a>(self) -\> <a href="struct.IntoKeys.html" class="struct"
title="struct hashbrown::hash_map::IntoKeys">IntoKeys</a>\<K, V, A\> <a href="#" class="tooltip"
data-notable-ty="IntoKeys&lt;K, V, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Creates a consuming iterator visiting all the keys in arbitrary order.
The map cannot be used after calling this. The iterator element type is
`K`.

##### <a href="#examples-18" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);

let mut vec: Vec<&str> = map.into_keys().collect();

// The `IntoKeys` iterator produces keys in arbitrary order, so the
// keys must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, ["a", "b", "c"]);
```

</div>

</div>

<div id="method.into_values" class="section method">

<a href="../../src/hashbrown/map.rs.html#976-980"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_values" class="fn">into_values</a>(self) -\> <a href="struct.IntoValues.html" class="struct"
title="struct hashbrown::hash_map::IntoValues">IntoValues</a>\<K, V, A\> <a href="#" class="tooltip"
data-notable-ty="IntoValues&lt;K, V, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Creates a consuming iterator visiting all the values in arbitrary order.
The map cannot be used after calling this. The iterator element type is
`V`.

##### <a href="#examples-19" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
map.insert("a", 1);
map.insert("b", 2);
map.insert("c", 3);

let mut vec: Vec<i32> = map.into_values().collect();

// The `IntoValues` iterator produces values in arbitrary order, so
// the values must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, [1, 2, 3]);
```

</div>

</div>

</div>

<div id="impl-HashMap%3CK,+V,+S,+A%3E-1" class="section impl">

<a href="../../src/hashbrown/map.rs.html#983-1862"
class="src rightside">Source</a><a href="#impl-HashMap%3CK,+V,+S,+A%3E-1" class="anchor">§</a>

### impl\<K, V, S, A\> <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where K:
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

<a href="../../src/hashbrown/map.rs.html#1013-1016"
class="src rightside">Source</a>

#### pub fn <a href="#method.reserve" class="fn">reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Reserves capacity for at least `additional` more elements to be inserted
in the `HashMap`. The collection may reserve more space to avoid
frequent reallocations.

##### <a href="#panics" class="doc-anchor">§</a>Panics

Panics if the new allocation size overflows
[`usize`](https://doc.rust-lang.org/std/primitive.usize.html).

##### <a href="#examples-20" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
let mut map: HashMap<&str, i32> = HashMap::new();
// Map is empty and doesn't allocate memory
assert_eq!(map.capacity(), 0);

map.reserve(10);

// And now map can hold at least 10 elements
assert!(map.capacity() >= 10);
```

</div>

</div>

<div id="method.try_reserve" class="section method">

<a href="../../src/hashbrown/map.rs.html#1063-1066"
class="src rightside">Source</a>

#### pub fn <a href="#method.try_reserve" class="fn">try_reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.unit.html"
class="primitive">()</a>, <a href="../enum.TryReserveError.html" class="enum"
title="enum hashbrown::TryReserveError">TryReserveError</a>\>

</div>

<div class="docblock">

Tries to reserve capacity for at least `additional` more elements to be
inserted in the given `HashMap<K,V>`. The collection may reserve more
space to avoid frequent reallocations.

##### <a href="#errors" class="doc-anchor">§</a>Errors

If the capacity overflows, or the allocator reports a failure, then an
error is returned.

##### <a href="#examples-21" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<&str, isize> = HashMap::new();
// Map is empty and doesn't allocate memory
assert_eq!(map.capacity(), 0);

map.try_reserve(10).expect("why is the test harness OOMing on 10 bytes?");

// And now map can hold at least 10 elements
assert!(map.capacity() >= 10);
```

</div>

If the capacity overflows, or the allocator reports a failure, then an
error is returned:

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::TryReserveError;
let mut map: HashMap<i32, i32> = HashMap::new();

match map.try_reserve(usize::MAX) {
    Err(error) => match error {
        TryReserveError::CapacityOverflow => {}
        _ => panic!("TryReserveError::AllocError ?"),
    },
    _ => panic!(),
}
```

</div>

</div>

<div id="method.shrink_to_fit" class="section method">

<a href="../../src/hashbrown/map.rs.html#1085-1088"
class="src rightside">Source</a>

#### pub fn <a href="#method.shrink_to_fit" class="fn">shrink_to_fit</a>(&mut self)

</div>

<div class="docblock">

Shrinks the capacity of the map as much as possible. It will drop down
as much as possible while maintaining the internal rules and possibly
leaving some space in accordance with the resize policy.

##### <a href="#examples-22" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<i32, i32> = HashMap::with_capacity(100);
map.insert(1, 2);
map.insert(3, 4);
assert!(map.capacity() >= 100);
map.shrink_to_fit();
assert!(map.capacity() >= 2);
```

</div>

</div>

<div id="method.shrink_to" class="section method">

<a href="../../src/hashbrown/map.rs.html#1114-1117"
class="src rightside">Source</a>

#### pub fn <a href="#method.shrink_to" class="fn">shrink_to</a>(&mut self, min_capacity: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Shrinks the capacity of the map with a lower limit. It will drop down no
lower than the supplied limit while maintaining the internal rules and
possibly leaving some space in accordance with the resize policy.

This function does nothing if the current capacity is smaller than the
supplied minimum capacity.

##### <a href="#examples-23" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map: HashMap<i32, i32> = HashMap::with_capacity(100);
map.insert(1, 2);
map.insert(3, 4);
assert!(map.capacity() >= 100);
map.shrink_to(10);
assert!(map.capacity() >= 10);
map.shrink_to(0);
assert!(map.capacity() >= 2);
map.shrink_to(10);
assert!(map.capacity() >= 2);
```

</div>

</div>

<div id="method.entry" class="section method">

<a href="../../src/hashbrown/map.rs.html#1139-1155"
class="src rightside">Source</a>

#### pub fn <a href="#method.entry" class="fn">entry</a>(&mut self, key: K) -\> <a href="enum.Entry.html" class="enum"
title="enum hashbrown::hash_map::Entry">Entry</a>\<'\_, K, V, S, A\>

</div>

<div class="docblock">

Gets the given key’s corresponding entry in the map for in-place
manipulation.

##### <a href="#examples-24" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut letters = HashMap::new();

for ch in "a short treatise on fungi".chars() {
    let counter = letters.entry(ch).or_insert(0);
    *counter += 1;
}

assert_eq!(letters[&'s'], 2);
assert_eq!(letters[&'t'], 3);
assert_eq!(letters[&'u'], 1);
assert_eq!(letters.get(&'y'), None);
```

</div>

</div>

<div id="method.entry_ref" class="section method">

<a href="../../src/hashbrown/map.rs.html#1175-1195"
class="src rightside">Source</a>

#### pub fn <a href="#method.entry_ref" class="fn">entry_ref</a>\<'a, 'b, Q\>( &'a mut self, key: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'b Q</a>, ) -\> <a href="enum.EntryRef.html" class="enum"
title="enum hashbrown::hash_map::EntryRef">EntryRef</a>\<'a, 'b, K, Q, V, S, A\>

<div class="where">

where K:
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

Gets the given key’s corresponding entry by reference in the map for
in-place manipulation.

##### <a href="#examples-25" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut words: HashMap<String, usize> = HashMap::new();
let source = ["poneyland", "horseyland", "poneyland", "poneyland"];
for (i, &s) in source.iter().enumerate() {
    let counter = words.entry_ref(s).or_insert(0);
    *counter += 1;
}

assert_eq!(words["poneyland"], 3);
assert_eq!(words["horseyland"], 1);
```

</div>

</div>

<div id="method.get" class="section method">

<a href="../../src/hashbrown/map.rs.html#1217-1227"
class="src rightside">Source</a>

#### pub fn <a href="#method.get" class="fn">get</a>\<Q\>(&self, k: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;V</a>\>

<div class="where">

where K:
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

Returns a reference to the value corresponding to the key.

The key may be any borrowed form of the map’s key type, but
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) and
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) on the borrowed
form *must* match those for the key type.

##### <a href="#examples-26" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
map.insert(1, "a");
assert_eq!(map.get(&1), Some(&"a"));
assert_eq!(map.get(&2), None);
```

</div>

</div>

<div id="method.get_key_value" class="section method">

<a href="../../src/hashbrown/map.rs.html#1249-1259"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_key_value" class="fn">get_key_value</a>\<Q\>(&self, k: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;V</a>)\>

<div class="where">

where K:
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

Returns the key-value pair corresponding to the supplied key.

The supplied key may be any borrowed form of the map’s key type, but
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) and
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) on the borrowed
form *must* match those for the key type.

##### <a href="#examples-27" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
map.insert(1, "a");
assert_eq!(map.get_key_value(&1), Some((&1, &"a")));
assert_eq!(map.get_key_value(&2), None);
```

</div>

</div>

<div id="method.get_key_value_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#1299-1309"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_key_value_mut" class="fn">get_key_value_mut</a>\<Q\>(&mut self, k: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>)\>

<div class="where">

where K:
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

Returns the key-value pair corresponding to the supplied key, with a
mutable reference to value.

The supplied key may be any borrowed form of the map’s key type, but
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) and
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) on the borrowed
form *must* match those for the key type.

##### <a href="#examples-28" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
map.insert(1, "a");
let (k, v) = map.get_key_value_mut(&1).unwrap();
assert_eq!(k, &1);
assert_eq!(v, &mut "a");
*v = "b";
assert_eq!(map.get_key_value_mut(&1), Some((&1, &mut "b")));
assert_eq!(map.get_key_value_mut(&2), None);
```

</div>

</div>

<div id="method.contains_key" class="section method">

<a href="../../src/hashbrown/map.rs.html#1331-1337"
class="src rightside">Source</a>

#### pub fn <a href="#method.contains_key" class="fn">contains_key</a>\<Q\>(&self, k: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where K:
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

Returns `true` if the map contains a value for the specified key.

The key may be any borrowed form of the map’s key type, but
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) and
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) on the borrowed
form *must* match those for the key type.

##### <a href="#examples-29" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
map.insert(1, "a");
assert_eq!(map.contains_key(&1), true);
assert_eq!(map.contains_key(&2), false);
```

</div>

</div>

<div id="method.get_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#1363-1373"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_mut" class="fn">get_mut</a>\<Q\>(&mut self, k: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>\>

<div class="where">

where K:
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

Returns a mutable reference to the value corresponding to the key.

The key may be any borrowed form of the map’s key type, but
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) and
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) on the borrowed
form *must* match those for the key type.

##### <a href="#examples-30" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
map.insert(1, "a");
if let Some(x) = map.get_mut(&1) {
    *x = "b";
}
assert_eq!(map[&1], "b");

assert_eq!(map.get_mut(&2), None);
```

</div>

</div>

<div id="method.get_many_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#1432-1438"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_many_mut" class="fn">get_many_mut</a>\<Q, const N: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>\>( &mut self, ks: \[<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>; <a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\], ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<\[<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>; <a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\]\>

<div class="where">

where K:
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

Attempts to get mutable references to `N` values in the map at once.

Returns an array of length `N` with the results of each query. For
soundness, at most one mutable reference will be returned to any value.
`None` will be returned if any of the keys are duplicates or missing.

##### <a href="#examples-31" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut libraries = HashMap::new();
libraries.insert("Bodleian Library".to_string(), 1602);
libraries.insert("Athenæum".to_string(), 1807);
libraries.insert("Herzogin-Anna-Amalia-Bibliothek".to_string(), 1691);
libraries.insert("Library of Congress".to_string(), 1800);

let got = libraries.get_many_mut([
    "Athenæum",
    "Library of Congress",
]);
assert_eq!(
    got,
    Some([
        &mut 1807,
        &mut 1800,
    ]),
);

// Missing keys result in None
let got = libraries.get_many_mut([
    "Athenæum",
    "New York Public Library",
]);
assert_eq!(got, None);

// Duplicate keys result in None
let got = libraries.get_many_mut([
    "Athenæum",
    "Athenæum",
]);
assert_eq!(got, None);
```

</div>

</div>

<div id="method.get_many_unchecked_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#1485-1495"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.get_many_unchecked_mut"
class="fn">get_many_unchecked_mut</a>\<Q, const N: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>\>( &mut self, ks: \[<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>; <a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\], ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<\[<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>; <a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\]\>

<div class="where">

where K:
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

Attempts to get mutable references to `N` values in the map at once,
without validating that the values are unique.

Returns an array of length `N` with the results of each query. `None`
will be returned if any of the keys are missing.

For a safe alternative see
[`get_many_mut`](../struct.HashMap.html#method.get_many_mut "method hashbrown::HashMap::get_many_mut").

##### <a href="#safety" class="doc-anchor">§</a>Safety

Calling this method with overlapping keys is *[undefined
behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html)*
even if the resulting references are not used.

##### <a href="#examples-32" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut libraries = HashMap::new();
libraries.insert("Bodleian Library".to_string(), 1602);
libraries.insert("Athenæum".to_string(), 1807);
libraries.insert("Herzogin-Anna-Amalia-Bibliothek".to_string(), 1691);
libraries.insert("Library of Congress".to_string(), 1800);

let got = libraries.get_many_mut([
    "Athenæum",
    "Library of Congress",
]);
assert_eq!(
    got,
    Some([
        &mut 1807,
        &mut 1800,
    ]),
);

// Missing keys result in None
let got = libraries.get_many_mut([
    "Athenæum",
    "New York Public Library",
]);
assert_eq!(got, None);
```

</div>

</div>

<div id="method.get_many_key_value_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#1541-1551"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_many_key_value_mut"
class="fn">get_many_key_value_mut</a>\<Q, const N: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>\>( &mut self, ks: \[<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>; <a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\], ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<\[(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>); <a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\]\>

<div class="where">

where K:
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

Attempts to get mutable references to `N` values in the map at once,
with immutable references to the corresponding keys.

Returns an array of length `N` with the results of each query. For
soundness, at most one mutable reference will be returned to any value.
`None` will be returned if any of the keys are duplicates or missing.

##### <a href="#examples-33" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut libraries = HashMap::new();
libraries.insert("Bodleian Library".to_string(), 1602);
libraries.insert("Athenæum".to_string(), 1807);
libraries.insert("Herzogin-Anna-Amalia-Bibliothek".to_string(), 1691);
libraries.insert("Library of Congress".to_string(), 1800);

let got = libraries.get_many_key_value_mut([
    "Bodleian Library",
    "Herzogin-Anna-Amalia-Bibliothek",
]);
assert_eq!(
    got,
    Some([
        (&"Bodleian Library".to_string(), &mut 1602),
        (&"Herzogin-Anna-Amalia-Bibliothek".to_string(), &mut 1691),
    ]),
);
// Missing keys result in None
let got = libraries.get_many_key_value_mut([
    "Bodleian Library",
    "Gewandhaus",
]);
assert_eq!(got, None);

// Duplicate keys result in None
let got = libraries.get_many_key_value_mut([
    "Bodleian Library",
    "Herzogin-Anna-Amalia-Bibliothek",
    "Herzogin-Anna-Amalia-Bibliothek",
]);
assert_eq!(got, None);
```

</div>

</div>

<div id="method.get_many_key_value_unchecked_mut"
class="section method">

<a href="../../src/hashbrown/map.rs.html#1597-1607"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.get_many_key_value_unchecked_mut"
class="fn">get_many_key_value_unchecked_mut</a>\<Q, const N: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>\>( &mut self, ks: \[<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>; <a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\], ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<\[(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>); <a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\]\>

<div class="where">

where K:
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

Attempts to get mutable references to `N` values in the map at once,
with immutable references to the corresponding keys, without validating
that the values are unique.

Returns an array of length `N` with the results of each query. `None`
will be returned if any of the keys are missing.

For a safe alternative see
[`get_many_key_value_mut`](../struct.HashMap.html#method.get_many_key_value_mut "method hashbrown::HashMap::get_many_key_value_mut").

##### <a href="#safety-1" class="doc-anchor">§</a>Safety

Calling this method with overlapping keys is *[undefined
behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html)*
even if the resulting references are not used.

##### <a href="#examples-34" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut libraries = HashMap::new();
libraries.insert("Bodleian Library".to_string(), 1602);
libraries.insert("Athenæum".to_string(), 1807);
libraries.insert("Herzogin-Anna-Amalia-Bibliothek".to_string(), 1691);
libraries.insert("Library of Congress".to_string(), 1800);

let got = libraries.get_many_key_value_mut([
    "Bodleian Library",
    "Herzogin-Anna-Amalia-Bibliothek",
]);
assert_eq!(
    got,
    Some([
        (&"Bodleian Library".to_string(), &mut 1602),
        (&"Herzogin-Anna-Amalia-Bibliothek".to_string(), &mut 1691),
    ]),
);
// Missing keys result in None
let got = libraries.get_many_key_value_mut([
    "Bodleian Library",
    "Gewandhaus",
]);
assert_eq!(got, None);
```

</div>

</div>

<div id="method.insert" class="section method">

<a href="../../src/hashbrown/map.rs.html#1674-1683"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(&mut self, k: K, v: V) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<V\>

</div>

<div class="docblock">

Inserts a key-value pair into the map.

If the map did not have this key present,
[`None`](https://doc.rust-lang.org/std/option/enum.Option.html#variant.None)
is returned.

If the map did have this key present, the value is updated, and the old
value is returned. The key is not updated, though; this matters for
types that can be `==` without being identical. See the
[`std::collections`](https://doc.rust-lang.org/std/collections/index.html)
[module-level
documentation](https://doc.rust-lang.org/std/collections/index.html#insert-and-complex-keys)
for more.

##### <a href="#examples-35" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
assert_eq!(map.insert(37, "a"), None);
assert_eq!(map.is_empty(), false);

map.insert(37, "b");
assert_eq!(map.insert(37, "c"), Some("b"));
assert_eq!(map[&37], "c");
```

</div>

</div>

<div id="method.insert_unique_unchecked" class="section method">

<a href="../../src/hashbrown/map.rs.html#1735-1742"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert_unique_unchecked"
class="fn">insert_unique_unchecked</a>(&mut self, k: K, v: V) -\> (<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>)

</div>

<div class="docblock">

Insert a key-value pair into the map without checking if the key already
exists in the map.

Returns a reference to the key and value just inserted.

This operation is safe if a key does not exist in the map.

However, if a key exists in the map already, the behavior is
unspecified: this operation may panic, loop forever, or any following
operation with the map may panic, loop forever or return arbitrary
result.

That said, this operation (and following operations) are guaranteed to
not violate memory safety.

This operation is faster than regular insert, because it does not
perform lookup before insertion.

This operation is useful during initial population of the map. For
example, when constructing a map from another map, we know that keys are
unique.

##### <a href="#examples-36" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map1 = HashMap::new();
assert_eq!(map1.insert(1, "a"), None);
assert_eq!(map1.insert(2, "b"), None);
assert_eq!(map1.insert(3, "c"), None);
assert_eq!(map1.len(), 3);

let mut map2 = HashMap::new();

for (key, value) in map1.into_iter() {
    map2.insert_unique_unchecked(key, value);
}

let (key, value) = map2.insert_unique_unchecked(4, "d");
assert_eq!(key, &4);
assert_eq!(value, &mut "d");
*value = "e";

assert_eq!(map2[&1], "a");
assert_eq!(map2[&2], "b");
assert_eq!(map2[&3], "c");
assert_eq!(map2[&4], "e");
assert_eq!(map2.len(), 4);
```

</div>

</div>

<div id="method.try_insert" class="section method">

<a href="../../src/hashbrown/map.rs.html#1773-1782"
class="src rightside">Source</a>

#### pub fn <a href="#method.try_insert" class="fn">try_insert</a>( &mut self, key: K, value: V, ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut V</a>, <a href="struct.OccupiedError.html" class="struct"
title="struct hashbrown::hash_map::OccupiedError">OccupiedError</a>\<'\_, K, V, S, A\>\>

</div>

<div class="docblock">

Tries to insert a key-value pair into the map, and returns a mutable
reference to the value in the entry.

##### <a href="#errors-1" class="doc-anchor">§</a>Errors

If the map already had this key present, nothing is updated, and an
error containing the occupied entry and the value is returned.

##### <a href="#examples-37" class="doc-anchor">§</a>Examples

Basic usage:

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use hashbrown::hash_map::OccupiedError;

let mut map = HashMap::new();
assert_eq!(map.try_insert(37, "a").unwrap(), &"a");

match map.try_insert(37, "b") {
    Err(OccupiedError { entry, value }) => {
        assert_eq!(entry.key(), &37);
        assert_eq!(entry.get(), &"a");
        assert_eq!(value, "b");
    }
    _ => panic!()
}
```

</div>

</div>

<div id="method.remove" class="section method">

<a href="../../src/hashbrown/map.rs.html#1813-1823"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove" class="fn">remove</a>\<Q\>(&mut self, k: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<V\>

<div class="where">

where K:
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

Removes a key from the map, returning the value at the key if the key
was previously in the map. Keeps the allocated memory for reuse.

The key may be any borrowed form of the map’s key type, but
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) and
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) on the borrowed
form *must* match those for the key type.

##### <a href="#examples-38" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
// The map is empty
assert!(map.is_empty() && map.capacity() == 0);

map.insert(1, "a");
let capacity_before_remove = map.capacity();

assert_eq!(map.remove(&1), Some("a"));
assert_eq!(map.remove(&1), None);

// Now map holds none elements but capacity is equal to the old one
assert!(map.len() == 0 && map.capacity() == capacity_before_remove);
```

</div>

</div>

<div id="method.remove_entry" class="section method">

<a href="../../src/hashbrown/map.rs.html#1854-1861"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove_entry" class="fn">remove_entry</a>\<Q\>(&mut self, k: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>\>

<div class="where">

where K:
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

Removes a key from the map, returning the stored key and value if the
key was previously in the map. Keeps the allocated memory for reuse.

The key may be any borrowed form of the map’s key type, but
[`Hash`](https://doc.rust-lang.org/std/hash/trait.Hash.html) and
[`Eq`](https://doc.rust-lang.org/std/cmp/trait.Eq.html) on the borrowed
form *must* match those for the key type.

##### <a href="#examples-39" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let mut map = HashMap::new();
// The map is empty
assert!(map.is_empty() && map.capacity() == 0);

map.insert(1, "a");
let capacity_before_remove = map.capacity();

assert_eq!(map.remove_entry(&1), Some((1, "a")));
assert_eq!(map.remove(&1), None);

// Now map hold none elements but capacity is equal to the old one
assert!(map.len() == 0 && map.capacity() == capacity_before_remove);
```

</div>

</div>

</div>

<div id="impl-HashMap%3CK,+V,+S,+A%3E-2" class="section impl">

<a href="../../src/hashbrown/map.rs.html#1864-2076"
class="src rightside">Source</a><a href="#impl-HashMap%3CK,+V,+S,+A%3E-2" class="anchor">§</a>

### impl\<K, V, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.raw_entry_mut" class="section method">

<a href="../../src/hashbrown/map.rs.html#1963-1965"
class="src rightside">Source</a>

#### pub fn <a href="#method.raw_entry_mut" class="fn">raw_entry_mut</a>(&mut self) -\> <a href="struct.RawEntryBuilderMut.html" class="struct"
title="struct hashbrown::hash_map::RawEntryBuilderMut">RawEntryBuilderMut</a>\<'\_, K, V, S, A\>

</div>

<div class="docblock">

Creates a raw entry builder for the HashMap.

Raw entries provide the lowest level of control for searching and
manipulating a map. They must be manually initialized with a hash and
then manually searched. After this, insertions into a vacant entry still
require an owned key to be provided.

Raw entries are useful for such exotic situations as:

- Hash memoization
- Deferring the creation of an owned key until it is known to be
  required
- Using a search key that doesn’t work with the Borrow trait
- Using custom comparison logic without newtype wrappers

Because raw entries provide much more low-level control, it’s much
easier to put the HashMap into an inconsistent state which, while
memory-safe, will cause the map to produce seemingly random results.
Higher-level and more foolproof APIs like `entry` should be preferred
when possible.

In particular, the hash used to initialized the raw entry must still be
consistent with the hash of the key that is ultimately stored in the
entry. This is because implementations of HashMap may need to recompute
hashes when resizing, at which point only the keys are available.

Raw entries give mutable access to the keys. This must not be used to
modify how the key would compare or hash, as the map will not
re-evaluate where the key should go, meaning the keys may become “lost”
if their location does not reflect their state. For instance, if you
change a key so that the map now contains keys which compare equal,
search may start acting erratically, with two keys randomly masking each
other. Implementations are free to assume this doesn’t happen (within
the limits of memory-safety).

##### <a href="#examples-40" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use core::hash::{BuildHasher, Hash};
use hashbrown::hash_map::{HashMap, RawEntryMut};

let mut map = HashMap::new();
map.extend([("a", 100), ("b", 200), ("c", 300)]);

fn compute_hash<K: Hash + ?Sized, S: BuildHasher>(hash_builder: &S, key: &K) -> u64 {
    use core::hash::Hasher;
    let mut state = hash_builder.build_hasher();
    key.hash(&mut state);
    state.finish()
}

// Existing key (insert and update)
match map.raw_entry_mut().from_key(&"a") {
    RawEntryMut::Vacant(_) => unreachable!(),
    RawEntryMut::Occupied(mut view) => {
        assert_eq!(view.get(), &100);
        let v = view.get_mut();
        let new_v = (*v) * 10;
        *v = new_v;
        assert_eq!(view.insert(1111), 1000);
    }
}

assert_eq!(map[&"a"], 1111);
assert_eq!(map.len(), 3);

// Existing key (take)
let hash = compute_hash(map.hasher(), &"c");
match map.raw_entry_mut().from_key_hashed_nocheck(hash, &"c") {
    RawEntryMut::Vacant(_) => unreachable!(),
    RawEntryMut::Occupied(view) => {
        assert_eq!(view.remove_entry(), ("c", 300));
    }
}
assert_eq!(map.raw_entry().from_key(&"c"), None);
assert_eq!(map.len(), 2);

// Nonexistent key (insert and update)
let key = "d";
let hash = compute_hash(map.hasher(), &key);
match map.raw_entry_mut().from_hash(hash, |q| *q == key) {
    RawEntryMut::Occupied(_) => unreachable!(),
    RawEntryMut::Vacant(view) => {
        let (k, value) = view.insert("d", 4000);
        assert_eq!((*k, *value), ("d", 4000));
        *value = 40000;
    }
}
assert_eq!(map[&"d"], 40000);
assert_eq!(map.len(), 3);

match map.raw_entry_mut().from_hash(hash, |q| *q == key) {
    RawEntryMut::Vacant(_) => unreachable!(),
    RawEntryMut::Occupied(view) => {
        assert_eq!(view.remove_entry(), ("d", 40000));
    }
}
assert_eq!(map.get(&"d"), None);
assert_eq!(map.len(), 2);
```

</div>

</div>

<div id="method.raw_entry" class="section method">

<a href="../../src/hashbrown/map.rs.html#2012-2014"
class="src rightside">Source</a>

#### pub fn <a href="#method.raw_entry" class="fn">raw_entry</a>(&self) -\> <a href="struct.RawEntryBuilder.html" class="struct"
title="struct hashbrown::hash_map::RawEntryBuilder">RawEntryBuilder</a>\<'\_, K, V, S, A\>

</div>

<div class="docblock">

Creates a raw immutable entry builder for the HashMap.

Raw entries provide the lowest level of control for searching and
manipulating a map. They must be manually initialized with a hash and
then manually searched.

This is useful for

- Hash memoization
- Using a search key that doesn’t work with the Borrow trait
- Using custom comparison logic without newtype wrappers

Unless you are in such a situation, higher-level and more foolproof APIs
like `get` should be preferred.

Immutable raw entries have very limited use; you might instead want
`raw_entry_mut`.

##### <a href="#examples-41" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use core::hash::{BuildHasher, Hash};
use hashbrown::HashMap;

let mut map = HashMap::new();
map.extend([("a", 100), ("b", 200), ("c", 300)]);

fn compute_hash<K: Hash + ?Sized, S: BuildHasher>(hash_builder: &S, key: &K) -> u64 {
    use core::hash::Hasher;
    let mut state = hash_builder.build_hasher();
    key.hash(&mut state);
    state.finish()
}

for k in ["a", "b", "c", "d", "e", "f"] {
    let hash = compute_hash(map.hasher(), k);
    let v = map.get(&k).cloned();
    let kv = v.as_ref().map(|v| (&k, v));

    println!("Key: {} and value: {:?}", k, v);

    assert_eq!(map.raw_entry().from_key(&k), kv);
    assert_eq!(map.raw_entry().from_hash(hash, |q| *q == k), kv);
    assert_eq!(map.raw_entry().from_key_hashed_nocheck(hash, &k), kv);
}
```

</div>

</div>

<div id="method.raw_table" class="section method">

<a href="../../src/hashbrown/map.rs.html#2073-2075"
class="src rightside">Source</a>

#### pub fn <a href="#method.raw_table" class="fn">raw_table</a>(&mut self) -\> &mut <a href="../raw/struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>, A\>

</div>

<div class="docblock">

Returns a mutable reference to the
[`RawTable`](raw/struct.RawTable.html) used underneath
[`HashMap`](struct.HashMap.html). This function is only available if the
`raw` feature of the crate is enabled.

##### <a href="#note" class="doc-anchor">§</a>Note

Calling the function safe, but using raw hash table API’s may require
unsafe functions or blocks.

`RawTable` API gives the lowest level of control under the map that can
be useful for extending the HashMap’s API, but may lead to *[undefined
behavior](https://doc.rust-lang.org/reference/behavior-considered-undefined.html)*.

##### <a href="#examples-42" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use core::hash::{BuildHasher, Hash};
use hashbrown::HashMap;

let mut map = HashMap::new();
map.extend([("a", 10), ("b", 20), ("c", 30)]);
assert_eq!(map.len(), 3);

// Let's imagine that we have a value and a hash of the key, but not the key itself.
// However, if you want to remove the value from the map by hash and value, and you
// know exactly that the value is unique, then you can create a function like this:
fn remove_by_hash<K, V, S, F>(
    map: &mut HashMap<K, V, S>,
    hash: u64,
    is_match: F,
) -> Option<(K, V)>
where
    F: Fn(&(K, V)) -> bool,
{
    let raw_table = map.raw_table();
    match raw_table.find(hash, is_match) {
        Some(bucket) => Some(unsafe { raw_table.remove(bucket) }),
        None => None,
    }
}

fn compute_hash<K: Hash + ?Sized, S: BuildHasher>(hash_builder: &S, key: &K) -> u64 {
    use core::hash::Hasher;
    let mut state = hash_builder.build_hasher();
    key.hash(&mut state);
    state.finish()
}

let hash = compute_hash(map.hasher(), "a");
assert_eq!(remove_by_hash(&mut map, hash, |(_, v)| *v == 10), Some(("a", 10)));
assert_eq!(map.get(&"a"), None);
assert_eq!(map.len(), 2);
```

</div>

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-HashMap%3CK,+V,+S,+A%3E" class="section impl">

<a href="../../src/hashbrown/map.rs.html#193-207"
class="src rightside">Source</a><a href="#impl-Clone-for-HashMap%3CK,+V,+S,+A%3E" class="anchor">§</a>

### impl\<K: <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, V: <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, S: <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#194-199"
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

<a href="../../src/hashbrown/map.rs.html#201-206"
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

<div id="impl-Debug-for-HashMap%3CK,+V,+S,+A%3E" class="section impl">

<a href="../../src/hashbrown/map.rs.html#2104-2113"
class="src rightside">Source</a><a href="#impl-Debug-for-HashMap%3CK,+V,+S,+A%3E" class="anchor">§</a>

### impl\<K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a>, A: Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#2110-2112"
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

<div id="impl-Default-for-HashMap%3CK,+V,+S,+A%3E" class="section impl">

<a href="../../src/hashbrown/map.rs.html#2115-2139"
class="src rightside">Source</a><a href="#impl-Default-for-HashMap%3CK,+V,+S,+A%3E" class="anchor">§</a>

### impl\<K, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

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

<a href="../../src/hashbrown/map.rs.html#2136-2138"
class="src rightside">Source</a><a href="#method.default" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html#tymethod.default"
class="fn">default</a>() -\> Self

</div>

<div class="docblock">

Creates an empty `HashMap<K, V, S, A>`, with the `Default` value for the
hasher and allocator.

##### <a href="#examples-43" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
use std::collections::hash_map::RandomState;

// You can specify all types of HashMap, including hasher and allocator.
// Created map is empty and don't allocate memory
let map: HashMap<u32, String> = Default::default();
assert_eq!(map.capacity(), 0);
let map: HashMap<u32, String, RandomState> = HashMap::default();
assert_eq!(map.capacity(), 0);
```

</div>

</div>

</div>

<div id="impl-Extend%3C%26(K,+V)%3E-for-HashMap%3CK,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#6501-6557"
class="src rightside">Source</a><a href="#impl-Extend%3C%26(K,+V)%3E-for-HashMap%3CK,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<&'a <a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>\> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>, A:
Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

<div class="docblock">

Inserts all new key-values from the iterator and replaces values with
existing keys with new values returned from the iterator.

</div>

</div>

<div class="impl-items">

<div id="method.extend-2" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#6542-6544"
class="src rightside">Source</a><a href="#method.extend-2" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<T: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = &'a <a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>\>\>(&mut self, iter: T)

</div>

<div class="docblock">

Inserts all new key-values from the iterator to existing
`HashMap<K, V, S, A>`. Replace values with existing keys with new values
returned from the iterator. The keys and values must implement
[`Copy`](https://doc.rust-lang.org/core/marker/trait.Copy.html) trait.

##### <a href="#examples-50" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::HashMap;

let mut map = HashMap::new();
map.insert(1, 100);

let arr = [(1, 1), (2, 2)];
let some_iter = arr.iter();
map.extend(some_iter);
// Replace values with existing keys with new values returned from the iterator.
// So that the map.get(&1) doesn't return Some(&100).
assert_eq!(map.get(&1), Some(&1));

let some_vec: Vec<_> = vec![(3, 3), (4, 4)];
map.extend(&some_vec);

let some_arr = [(5, 5), (6, 6)];
map.extend(&some_arr);

let mut vec: Vec<_> = map.into_iter().collect();
// The `IntoIter` iterator produces items in arbitrary order, so the
// items must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]);
```

</div>

</div>

<div id="method.extend_one-2" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#417"
class="src rightside">Source</a><a href="#method.extend_one-2" class="anchor">§</a>

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

<div id="method.extend_reserve-2" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#425"
class="src rightside">Source</a><a href="#method.extend_reserve-2" class="anchor">§</a>

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

<div id="impl-Extend%3C(%26K,+%26V)%3E-for-HashMap%3CK,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#6436-6497"
class="src rightside">Source</a><a href="#impl-Extend%3C(%26K,+%26V)%3E-for-HashMap%3CK,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a V</a>)\> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>, A:
Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

<div class="docblock">

Inserts all new key-values from the iterator and replaces values with
existing keys with new values returned from the iterator.

</div>

</div>

<div class="impl-items">

<div id="method.extend-1" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#6482-6484"
class="src rightside">Source</a><a href="#method.extend-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<T: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = (<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a V</a>)\>\>(&mut self, iter: T)

</div>

<div class="docblock">

Inserts all new key-values from the iterator to existing
`HashMap<K, V, S, A>`. Replace values with existing keys with new values
returned from the iterator. The keys and values must implement
[`Copy`](https://doc.rust-lang.org/core/marker/trait.Copy.html) trait.

##### <a href="#examples-49" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::HashMap;

let mut map = HashMap::new();
map.insert(1, 100);

let arr = [(1, 1), (2, 2)];
let some_iter = arr.iter().map(|&(k, v)| (k, v));
map.extend(some_iter);
// Replace values with existing keys with new values returned from the iterator.
// So that the map.get(&1) doesn't return Some(&100).
assert_eq!(map.get(&1), Some(&1));

let some_vec: Vec<_> = vec![(3, 3), (4, 4)];
map.extend(some_vec.iter().map(|&(k, v)| (k, v)));

let some_arr = [(5, 5), (6, 6)];
map.extend(some_arr.iter().map(|&(k, v)| (k, v)));

// You can also extend from another HashMap
let mut new_map = HashMap::new();
new_map.extend(&map);
assert_eq!(new_map, map);

let mut vec: Vec<_> = new_map.into_iter().collect();
// The `IntoIter` iterator produces items in arbitrary order, so the
// items must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]);
```

</div>

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

<div id="impl-Extend%3C(K,+V)%3E-for-HashMap%3CK,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#6353-6432"
class="src rightside">Source</a><a href="#impl-Extend%3C(K,+V)%3E-for-HashMap%3CK,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>\> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where K:
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

<div class="docblock">

Inserts all new key-values from the iterator and replaces values with
existing keys with new values returned from the iterator.

</div>

</div>

<div class="impl-items">

<div id="method.extend" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#6395-6410"
class="src rightside">Source</a><a href="#method.extend" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<T: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = <a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>\>\>(&mut self, iter: T)

</div>

<div class="docblock">

Inserts all new key-values from the iterator to existing
`HashMap<K, V, S, A>`. Replace values with existing keys with new values
returned from the iterator.

##### <a href="#examples-48" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::hash_map::HashMap;

let mut map = HashMap::new();
map.insert(1, 100);

let some_iter = [(1, 1), (2, 2)].into_iter();
map.extend(some_iter);
// Replace values with existing keys with new values returned from the iterator.
// So that the map.get(&1) doesn't return Some(&100).
assert_eq!(map.get(&1), Some(&1));

let some_vec: Vec<_> = vec![(3, 3), (4, 4)];
map.extend(some_vec);

let some_arr = [(5, 5), (6, 6)];
map.extend(some_arr);
let old_map_len = map.len();

// You can also extend from another HashMap
let mut new_map = HashMap::new();
new_map.extend(map);
assert_eq!(new_map.len(), old_map_len);

let mut vec: Vec<_> = new_map.into_iter().collect();
// The `IntoIter` iterator produces items in arbitrary order, so the
// items must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]);
```

</div>

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

<a href="../../src/hashbrown/set.rs.html#1180-1187"
class="src rightside">Source</a><a
href="#impl-From%3CHashMap%3CT,+(),+S,+A%3E%3E-for-HashSet%3CT,+S,+A%3E"
class="anchor">§</a>

### impl\<T, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<T, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.unit.html"
class="primitive">()</a>, S, A\>\> for <a href="../struct.HashSet.html" class="struct"
title="struct hashbrown::HashSet">HashSet</a>\<T, S, A\>

<div class="where">

where A: Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a href="../../src/hashbrown/set.rs.html#1184-1186"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(map: <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<T, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.unit.html"
class="primitive">()</a>, S, A\>) -\> Self

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-FromIterator%3C(K,+V)%3E-for-HashMap%3CK,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#6333-6349"
class="src rightside">Source</a><a href="#impl-FromIterator%3C(K,+V)%3E-for-HashMap%3CK,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html"
class="trait"
title="trait core::iter::traits::collect::FromIterator">FromIterator</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>\> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where K:
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

<a href="../../src/hashbrown/map.rs.html#6340-6348"
class="src rightside">Source</a><a href="#method.from_iter" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html#tymethod.from_iter"
class="fn">from_iter</a>\<T: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = <a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>\>\>(iter: T) -\> Self

</div>

<div class="docblock">

Creates a value from an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html#tymethod.from_iter)

</div>

</div>

<div id="impl-Index%3C%26Q%3E-for-HashMap%3CK,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#2141-2170"
class="src rightside">Source</a><a href="#impl-Index%3C%26Q%3E-for-HashMap%3CK,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K, Q, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html"
class="trait" title="trait core::ops::index::Index">Index</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>\> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\>, Q:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>, A:
Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.index" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#2167-2169"
class="src rightside">Source</a><a href="#method.index" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html#tymethod.index"
class="fn">index</a>(&self, key: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;Q</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;V</a>

</div>

<div class="docblock">

Returns a reference to the value corresponding to the supplied key.

##### <a href="#panics-1" class="doc-anchor">§</a>Panics

Panics if the key is not present in the `HashMap`.

##### <a href="#examples-44" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let map: HashMap<_, _> = [("a", "One"), ("b", "Two")].into();

assert_eq!(map[&"a"], "One");
assert_eq!(map[&"b"], "Two");
```

</div>

</div>

<div id="associatedtype.Output"
class="section associatedtype trait-impl">

<a href="../../src/hashbrown/map.rs.html#2148"
class="src rightside">Source</a><a href="#associatedtype.Output" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/index/trait.Index.html#associatedtype.Output"
class="associatedtype">Output</a> = V

</div>

<div class="docblock">

The returned type after indexing.

</div>

</div>

<div id="impl-IntoIterator-for-%26HashMap%3CK,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#4570-4600"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-%26HashMap%3CK,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for &'a <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.into_iter" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#4597-4599"
class="src rightside">Source</a><a href="#method.into_iter" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter"
class="fn">into_iter</a>(self) -\> <a href="struct.Iter.html" class="struct"
title="struct hashbrown::hash_map::Iter">Iter</a>\<'a, K, V\> <a href="#" class="tooltip"
data-notable-ty="Iter&lt;&#39;a, K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

Creates an iterator over the entries of a `HashMap` in arbitrary order.
The iterator element type is `(&'a K, &'a V)`.

Return the same `Iter` struct as by the
[`iter`](struct.HashMap.html#method.iter) method on
[`HashMap`](struct.HashMap.html).

##### <a href="#examples-45" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
let map_one: HashMap<_, _> = [(1, "a"), (2, "b"), (3, "c")].into();
let mut map_two = HashMap::new();

for (key, value) in &map_one {
    println!("Key: {}, Value: {}", key, value);
    map_two.insert_unique_unchecked(*key, *value);
}

assert_eq!(map_one, map_two);
```

</div>

</div>

<div id="associatedtype.Item" class="section associatedtype trait-impl">

<a href="../../src/hashbrown/map.rs.html#4571"
class="src rightside">Source</a><a href="#associatedtype.Item" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = (<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a V</a>)

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter"
class="section associatedtype trait-impl">

<a href="../../src/hashbrown/map.rs.html#4572"
class="src rightside">Source</a><a href="#associatedtype.IntoIter" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="struct.Iter.html" class="struct"
title="struct hashbrown::hash_map::Iter">Iter</a>\<'a, K, V\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

</div>

<div id="impl-IntoIterator-for-%26mut+HashMap%3CK,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#4602-4637"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-%26mut+HashMap%3CK,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<'a, K, V, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for &'a mut <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.into_iter-1" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#4634-4636"
class="src rightside">Source</a><a href="#method.into_iter-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter"
class="fn">into_iter</a>(self) -\> <a href="struct.IterMut.html" class="struct"
title="struct hashbrown::hash_map::IterMut">IterMut</a>\<'a, K, V\> <a href="#" class="tooltip"
data-notable-ty="IterMut&lt;&#39;a, K, V&gt;">ⓘ</a>

</div>

<div class="docblock">

Creates an iterator over the entries of a `HashMap` in arbitrary order
with mutable references to the values. The iterator element type is
`(&'a K, &'a mut V)`.

Return the same `IterMut` struct as by the
[`iter_mut`](struct.HashMap.html#method.iter_mut) method on
[`HashMap`](struct.HashMap.html).

##### <a href="#examples-46" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;
let mut map: HashMap<_, _> = [("a", 1), ("b", 2), ("c", 3)].into();

for (key, value) in &mut map {
    println!("Key: {}, Value: {}", key, value);
    *value *= 2;
}

let mut vec = map.iter().collect::<Vec<_>>();
// The `Iter` iterator produces items in arbitrary order, so the
// items must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, [(&"a", &2), (&"b", &4), (&"c", &6)]);
```

</div>

</div>

<div id="associatedtype.Item-1"
class="section associatedtype trait-impl">

<a href="../../src/hashbrown/map.rs.html#4603"
class="src rightside">Source</a><a href="#associatedtype.Item-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = (<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a K</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;'a mut V</a>)

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter-1"
class="section associatedtype trait-impl">

<a href="../../src/hashbrown/map.rs.html#4604"
class="src rightside">Source</a><a href="#associatedtype.IntoIter-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="struct.IterMut.html" class="struct"
title="struct hashbrown::hash_map::IterMut">IterMut</a>\<'a, K, V\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

</div>

<div id="impl-IntoIterator-for-HashMap%3CK,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#4639-4667"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-HashMap%3CK,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K, V, S, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

</div>

<div class="impl-items">

<div id="method.into_iter-2" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#4662-4666"
class="src rightside">Source</a><a href="#method.into_iter-2" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter"
class="fn">into_iter</a>(self) -\> <a href="struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_map::IntoIter">IntoIter</a>\<K, V, A\> <a href="#" class="tooltip"
data-notable-ty="IntoIter&lt;K, V, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Creates a consuming iterator, that is, one that moves each key-value
pair out of the map in arbitrary order. The map cannot be used after
calling this.

##### <a href="#examples-47" class="doc-anchor">§</a>Examples

<div class="example-wrap">

``` rust
use hashbrown::HashMap;

let map: HashMap<_, _> = [("a", 1), ("b", 2), ("c", 3)].into();

// Not possible with .iter()
let mut vec: Vec<(&str, i32)> = map.into_iter().collect();
// The `IntoIter` iterator produces items in arbitrary order, so
// the items must be sorted to test them against a sorted array.
vec.sort_unstable();
assert_eq!(vec, [("a", 1), ("b", 2), ("c", 3)]);
```

</div>

</div>

<div id="associatedtype.Item-2"
class="section associatedtype trait-impl">

<a href="../../src/hashbrown/map.rs.html#4640"
class="src rightside">Source</a><a href="#associatedtype.Item-2" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = <a href="https://doc.rust-lang.org/1.92.0/core/primitive.tuple.html"
class="primitive">(K, V)</a>

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter-2"
class="section associatedtype trait-impl">

<a href="../../src/hashbrown/map.rs.html#4641"
class="src rightside">Source</a><a href="#associatedtype.IntoIter-2" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="struct.IntoIter.html" class="struct"
title="struct hashbrown::hash_map::IntoIter">IntoIter</a>\<K, V, A\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

</div>

<div id="impl-PartialEq-for-HashMap%3CK,+V,+S,+A%3E"
class="section impl">

<a href="../../src/hashbrown/map.rs.html#2078-2093"
class="src rightside">Source</a><a href="#impl-PartialEq-for-HashMap%3CK,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a>, S: <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.BuildHasher.html"
class="trait" title="trait core::hash::BuildHasher">BuildHasher</a>, A:
Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../../src/hashbrown/map.rs.html#2085-2092"
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

<div id="impl-Eq-for-HashMap%3CK,+V,+S,+A%3E" class="section impl">

<a href="../../src/hashbrown/map.rs.html#2095-2102"
class="src rightside">Source</a><a href="#impl-Eq-for-HashMap%3CK,+V,+S,+A%3E" class="anchor">§</a>

### impl\<K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where K:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a>, S: <a
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

<div id="impl-Freeze-for-HashMap%3CK,+V,+S,+A%3E" class="section impl">

<a href="#impl-Freeze-for-HashMap%3CK,+V,+S,+A%3E" class="anchor">§</a>

### impl\<K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>,

</div>

</div>

<div id="impl-RefUnwindSafe-for-HashMap%3CK,+V,+S,+A%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-HashMap%3CK,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where S: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
A: <a
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

<div id="impl-Send-for-HashMap%3CK,+V,+S,+A%3E" class="section impl">

<a href="#impl-Send-for-HashMap%3CK,+V,+S,+A%3E" class="anchor">§</a>

### impl\<K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-HashMap%3CK,+V,+S,+A%3E" class="section impl">

<a href="#impl-Sync-for-HashMap%3CK,+V,+S,+A%3E" class="anchor">§</a>

### impl\<K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>,

</div>

</div>

<div id="impl-Unpin-for-HashMap%3CK,+V,+S,+A%3E" class="section impl">

<a href="#impl-Unpin-for-HashMap%3CK,+V,+S,+A%3E" class="anchor">§</a>

### impl\<K, V, S, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where S:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, V:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-HashMap%3CK,+V,+S,+A%3E"
class="section impl">

<a href="#impl-UnwindSafe-for-HashMap%3CK,+V,+S,+A%3E"
class="anchor">§</a>

### impl\<K, V, S, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="../struct.HashMap.html" class="struct"
title="struct hashbrown::HashMap">HashMap</a>\<K, V, S, A\>

<div class="where">

where S: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a>, A: <a
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
