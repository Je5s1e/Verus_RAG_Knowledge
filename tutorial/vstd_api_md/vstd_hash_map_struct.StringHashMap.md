<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[hash_map](index.html)

</div>

# Struct <span class="struct">StringHashMap</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/hash_map.rs.html#189-191" class="src">Source</a>
</span>

</div>

``` rust
pub struct StringHashMap<Value> { /* private fields */ }
```

Expand description

<div class="docblock">

`StringHashMap` is a trusted wrapper around
`std::collections::HashMap<String, Value>` with `View` implemented for
the type `vstd::map::Map<Seq<char>, Value>`.

This type was created for ease of use with `String` as it uses `&str`
instead of `&String` for methods that require shared references. Also,
it assumes that
[`obeys_key_model::<String>()`](https://verus-lang.github.io/verus/verusdoc/vstd/std_specs/hash/fn.obeys_key_model.html)
holds.

See the Rust documentation for
[`HashMap`](https://doc.rust-lang.org/std/collections/struct.HashMap.html)
for details about its implementation.

If you are using `std::collections::HashMap` directly, see
[`ExHashMap`](https://verus-lang.github.io/verus/verusdoc/vstd/std_specs/hash/struct.ExHashMap.html)
for information on the Verus specifications for this type.

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-StringHashMap%3CValue%3E" class="section impl">

<a href="../../src/vstd/hash_map.rs.html#199-321"
class="src rightside">Source</a><a href="#impl-StringHashMap%3CValue%3E" class="anchor">§</a>

### impl\<Value\> <a href="struct.StringHashMap.html" class="struct"
title="struct vstd::hash_map::StringHashMap">StringHashMap</a>\<Value\>

</div>

<div class="impl-items">

<div id="method.new" class="section method">

<a href="../../src/vstd/hash_map.rs.html#204-209"
class="src rightside">Source</a>

#### pub fn <a href="#method.new" class="fn">new</a>() -\> Self

</div>

<div class="docblock">

Creates an empty `StringHashMap` with a capacity of 0.

See Rust’s
[`HashMap::new()`](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.new)
for implementation details.

</div>

<div id="method.with_capacity" class="section method">

<a href="../../src/vstd/hash_map.rs.html#215-220"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_capacity" class="fn">with_capacity</a>(capacity: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> Self

</div>

<div class="docblock">

Creates an empty `StringHashMap` with at least capacity for the
specified number of elements.

See Rust’s
[`HashMap::with_capacity()`](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.with_capacity)
for implementation details.

</div>

<div id="method.reserve" class="section method">

<a href="../../src/vstd/hash_map.rs.html#226-231"
class="src rightside">Source</a>

#### pub fn <a href="#method.reserve" class="fn">reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Reserves capacity for at least `additional` number of elements in the
map.

See Rust’s
[`HashMap::reserve()`](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.reserve)
for implementation details.

</div>

<div id="method.is_empty" class="section method">

<a href="../../src/vstd/hash_map.rs.html#235-240"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_empty" class="fn">is_empty</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns true if the map is empty.

</div>

<div id="method.len" class="section method">

<a href="../../src/vstd/hash_map.rs.html#248-253"
class="src rightside">Source</a>

#### pub fn <a href="#method.len" class="fn">len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Returns the number of elements in the map.

</div>

<div id="method.insert" class="section method">

<a href="../../src/vstd/hash_map.rs.html#259-264"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(&mut self, k: <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>, v: Value)

</div>

<div class="docblock">

Inserts the given key and value in the map.

See Rust’s
[`HashMap::insert()`](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.insert)
for implementation details.

</div>

<div id="method.remove" class="section method">

<a href="../../src/vstd/hash_map.rs.html#270-275"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove" class="fn">remove</a>(&mut self, k: &<a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>)

</div>

<div class="docblock">

Removes the given key from the map. If the key is not present in the
map, the map is unmodified.

See Rust’s
[`HashMap::remove()`](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.remove)
for implementation details.

</div>

<div id="method.contains_key" class="section method">

<a href="../../src/vstd/hash_map.rs.html#281-286"
class="src rightside">Source</a>

#### pub fn <a href="#method.contains_key" class="fn">contains_key</a>(&self, k: &<a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns true if the map contains the given key.

See Rust’s
[`HashMap::contains_key()`](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.contains_key)
for implementation details.

</div>

<div id="method.get" class="section method">

<a href="../../src/vstd/hash_map.rs.html#292-300"
class="src rightside">Source</a>

#### pub fn <a href="#method.get" class="fn">get</a>\<'a\>(&'a self, k: &<a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a Value</a>\>

</div>

<div class="docblock">

Returns a reference to the value corresponding to the given key in the
map. If the key is not present in the map, returns `None`.

See Rust’s
[`HashMap::get()`](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.get)
for implementation details.

</div>

<div id="method.clear" class="section method">

<a href="../../src/vstd/hash_map.rs.html#306-311"
class="src rightside">Source</a>

#### pub fn <a href="#method.clear" class="fn">clear</a>(&mut self)

</div>

<div class="docblock">

Clears all key-value pairs in the map. Retains the allocated memory for
reuse.

See Rust’s
[`HashMap::clear()`](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.clear)
for implementation details.

</div>

<div id="method.union_prefer_right" class="section method">

<a href="../../src/vstd/hash_map.rs.html#315-320"
class="src rightside">Source</a>

#### pub fn <a href="#method.union_prefer_right" class="fn">union_prefer_right</a>(&mut self, other: Self)

</div>

<div class="docblock">

Returns the union of the two maps. If a key is present in both maps,
then the value in the right map (`other`) is retained.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-View-for-StringHashMap%3CValue%3E" class="section impl">

<a href="../../src/vstd/hash_map.rs.html#193-197"
class="src rightside">Source</a><a href="#impl-View-for-StringHashMap%3CValue%3E" class="anchor">§</a>

### impl\<Value\> <a href="../view/trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="struct.StringHashMap.html" class="struct"
title="struct vstd::hash_map::StringHashMap">StringHashMap</a>\<Value\>

</div>

<div class="impl-items">

<div id="associatedtype.V" class="section associatedtype trait-impl">

<a href="../../src/vstd/hash_map.rs.html#194"
class="src rightside">Source</a><a href="#associatedtype.V" class="anchor">§</a>

#### type <a href="../view/trait.View.html#associatedtype.V"
class="associatedtype">V</a> = <a href="../map/struct.Map.html" class="struct"
title="struct vstd::map::Map">Map</a>\<<a href="../seq/struct.Seq.html" class="struct"
title="struct vstd::seq::Seq">Seq</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>\>, Value\>

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-StringHashMap%3CValue%3E" class="section impl">

<a href="#impl-Freeze-for-StringHashMap%3CValue%3E" class="anchor">§</a>

### impl\<Value\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.StringHashMap.html" class="struct"
title="struct vstd::hash_map::StringHashMap">StringHashMap</a>\<Value\>

</div>

<div id="impl-RefUnwindSafe-for-StringHashMap%3CValue%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-StringHashMap%3CValue%3E"
class="anchor">§</a>

### impl\<Value\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.StringHashMap.html" class="struct"
title="struct vstd::hash_map::StringHashMap">StringHashMap</a>\<Value\>

<div class="where">

where Value: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

<div id="impl-Send-for-StringHashMap%3CValue%3E" class="section impl">

<a href="#impl-Send-for-StringHashMap%3CValue%3E" class="anchor">§</a>

### impl\<Value\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.StringHashMap.html" class="struct"
title="struct vstd::hash_map::StringHashMap">StringHashMap</a>\<Value\>

<div class="where">

where Value:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-StringHashMap%3CValue%3E" class="section impl">

<a href="#impl-Sync-for-StringHashMap%3CValue%3E" class="anchor">§</a>

### impl\<Value\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.StringHashMap.html" class="struct"
title="struct vstd::hash_map::StringHashMap">StringHashMap</a>\<Value\>

<div class="where">

where Value:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>,

</div>

</div>

<div id="impl-Unpin-for-StringHashMap%3CValue%3E" class="section impl">

<a href="#impl-Unpin-for-StringHashMap%3CValue%3E" class="anchor">§</a>

### impl\<Value\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.StringHashMap.html" class="struct"
title="struct vstd::hash_map::StringHashMap">StringHashMap</a>\<Value\>

<div class="where">

where Value:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-StringHashMap%3CValue%3E"
class="section impl">

<a href="#impl-UnwindSafe-for-StringHashMap%3CValue%3E"
class="anchor">§</a>

### impl\<Value\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.StringHashMap.html" class="struct"
title="struct vstd::hash_map::StringHashMap">StringHashMap</a>\<Value\>

<div class="where">

where Value: <a
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

<div id="impl-From%3CT%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#785"
class="src rightside">Source</a><a href="#impl-From%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\> for T

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

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
