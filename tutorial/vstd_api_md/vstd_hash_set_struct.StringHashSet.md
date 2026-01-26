<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[hash_set](index.html)

</div>

# Struct <span class="struct">StringHashSet</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/hash_set.rs.html#180-182" class="src">Source</a>
</span>

</div>

``` rust
pub struct StringHashSet { /* private fields */ }
```

Expand description

<div class="docblock">

`StringHashSet` is a trusted wrapper around
`std::collections::HashSet<String>` with `View` implemented for the type
`vstd::map::Set<Seq<char>>`.

This type was created for ease of use with `String` as it uses `&str`
instead of `&String` for methods that require shared references. Also,
it assumes that
[`obeys_key_model::<String>()`](https://verus-lang.github.io/verus/verusdoc/vstd/std_specs/hash/fn.obeys_key_model.html)
holds.

See the Rust documentation for
[`HashSet`](https://doc.rust-lang.org/std/collections/struct.HashSet.html)
for details about its implementation.

If you are using `std::collections::HashSet` directly, see
[`ExHashSet`](https://verus-lang.github.io/verus/verusdoc/vstd/std_specs/hash/struct.ExHashSet.html)
for information on the Verus specifications for this type.

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-StringHashSet" class="section impl">

<a href="../../src/vstd/hash_set.rs.html#190-303"
class="src rightside">Source</a><a href="#impl-StringHashSet" class="anchor">§</a>

### impl <a href="struct.StringHashSet.html" class="struct"
title="struct vstd::hash_set::StringHashSet">StringHashSet</a>

</div>

<div class="impl-items">

<div id="method.new" class="section method">

<a href="../../src/vstd/hash_set.rs.html#195-200"
class="src rightside">Source</a>

#### pub fn <a href="#method.new" class="fn">new</a>() -\> Self

</div>

<div class="docblock">

Creates an empty `StringHashSet` with capacity 0.

See Rust’s
[`HashSet::new()`](https://doc.rust-lang.org/std/collections/struct.HashSet.html#method.new)
for implementation details.

</div>

<div id="method.with_capacity" class="section method">

<a href="../../src/vstd/hash_set.rs.html#206-211"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_capacity" class="fn">with_capacity</a>(capacity: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> Self

</div>

<div class="docblock">

Creates an empty `StringHashSet` with at least capacity for the
specified number of elements.

See Rust’s
[`HashSet::with_capacity()`](https://doc.rust-lang.org/std/collections/struct.HashSet.html#method.with_capacity)
for implementation details.

</div>

<div id="method.reserve" class="section method">

<a href="../../src/vstd/hash_set.rs.html#217-222"
class="src rightside">Source</a>

#### pub fn <a href="#method.reserve" class="fn">reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<div class="docblock">

Reserves capacity for at least `additional` number of elements in the
set.

See Rust’s
[`HashSet::reserve()`](https://doc.rust-lang.org/std/collections/struct.HashSet.html#method.reserve)
for implementation details.

</div>

<div id="method.is_empty" class="section method">

<a href="../../src/vstd/hash_set.rs.html#226-231"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_empty" class="fn">is_empty</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns true if the set is empty.

</div>

<div id="method.len" class="section method">

<a href="../../src/vstd/hash_set.rs.html#239-244"
class="src rightside">Source</a>

#### pub fn <a href="#method.len" class="fn">len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Returns the number of elements in the set.

</div>

<div id="method.insert" class="section method">

<a href="../../src/vstd/hash_set.rs.html#250-255"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>(&mut self, k: <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Inserts the given value into the set. Returns true if the value was not
previously in the set, false otherwise.

See Rust’s
[`HashSet::insert()`](https://doc.rust-lang.org/std/collections/struct.HashSet.html#method.insert)
for implementation details.

</div>

<div id="method.remove" class="section method">

<a href="../../src/vstd/hash_set.rs.html#261-266"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove" class="fn">remove</a>(&mut self, k: &<a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Removes the given value from the set. Returns true if the value was
previously in the set, false otherwise.

See Rust’s
[`HashSet::remove()`](https://doc.rust-lang.org/std/collections/struct.HashSet.html#method.remove)
for implementation details.

</div>

<div id="method.contains" class="section method">

<a href="../../src/vstd/hash_set.rs.html#272-277"
class="src rightside">Source</a>

#### pub fn <a href="#method.contains" class="fn">contains</a>(&self, k: &<a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns true if the set contains the given value.

See Rust’s
[`HashSet::contains()`](https://doc.rust-lang.org/std/collections/struct.HashSet.html#method.contains)
for implementation details.

</div>

<div id="method.get" class="section method">

<a href="../../src/vstd/hash_set.rs.html#283-291"
class="src rightside">Source</a>

#### pub fn <a href="#method.get" class="fn">get</a>\<'a\>(&'a self, k: &<a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<&'a <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>\>

</div>

<div class="docblock">

Returns a reference to the value in the set that is equal to the given
value. If the value is not present in the set, returns `None`.

See Rust’s
[`HashSet::get()`](https://doc.rust-lang.org/std/collections/struct.HashSet.html#method.get)
for implementation details.

</div>

<div id="method.clear" class="section method">

<a href="../../src/vstd/hash_set.rs.html#297-302"
class="src rightside">Source</a>

#### pub fn <a href="#method.clear" class="fn">clear</a>(&mut self)

</div>

<div class="docblock">

Clears all values from the set.

See Rust’s
[`HashSet::clear()`](https://doc.rust-lang.org/std/collections/struct.HashSet.html#method.clear)
for implementation details.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-View-for-StringHashSet" class="section impl">

<a href="../../src/vstd/hash_set.rs.html#184-188"
class="src rightside">Source</a><a href="#impl-View-for-StringHashSet" class="anchor">§</a>

### impl <a href="../view/trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="struct.StringHashSet.html" class="struct"
title="struct vstd::hash_set::StringHashSet">StringHashSet</a>

</div>

<div class="impl-items">

<div id="associatedtype.V" class="section associatedtype trait-impl">

<a href="../../src/vstd/hash_set.rs.html#185"
class="src rightside">Source</a><a href="#associatedtype.V" class="anchor">§</a>

#### type <a href="../view/trait.View.html#associatedtype.V"
class="associatedtype">V</a> = <a href="../set/struct.Set.html" class="struct"
title="struct vstd::set::Set">Set</a>\<<a href="../seq/struct.Seq.html" class="struct"
title="struct vstd::seq::Seq">Seq</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>\>\>

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-StringHashSet" class="section impl">

<a href="#impl-Freeze-for-StringHashSet" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.StringHashSet.html" class="struct"
title="struct vstd::hash_set::StringHashSet">StringHashSet</a>

</div>

<div id="impl-RefUnwindSafe-for-StringHashSet" class="section impl">

<a href="#impl-RefUnwindSafe-for-StringHashSet" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.StringHashSet.html" class="struct"
title="struct vstd::hash_set::StringHashSet">StringHashSet</a>

</div>

<div id="impl-Send-for-StringHashSet" class="section impl">

<a href="#impl-Send-for-StringHashSet" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.StringHashSet.html" class="struct"
title="struct vstd::hash_set::StringHashSet">StringHashSet</a>

</div>

<div id="impl-Sync-for-StringHashSet" class="section impl">

<a href="#impl-Sync-for-StringHashSet" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.StringHashSet.html" class="struct"
title="struct vstd::hash_set::StringHashSet">StringHashSet</a>

</div>

<div id="impl-Unpin-for-StringHashSet" class="section impl">

<a href="#impl-Unpin-for-StringHashSet" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.StringHashSet.html" class="struct"
title="struct vstd::hash_set::StringHashSet">StringHashSet</a>

</div>

<div id="impl-UnwindSafe-for-StringHashSet" class="section impl">

<a href="#impl-UnwindSafe-for-StringHashSet" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.StringHashSet.html" class="struct"
title="struct vstd::hash_set::StringHashSet">StringHashSet</a>

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
