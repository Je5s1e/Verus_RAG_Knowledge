<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[hashbrown](../index.html)::[raw](index.html)

</div>

# Struct <span class="struct">RawTable</span> Copy item path

<span class="sub-heading"><a href="../../src/hashbrown/raw/mod.rs.html#361-365"
class="src">Source</a> </span>

</div>

``` rust
pub struct RawTable<T, A: Allocator + Clone = Global> { /* private fields */ }
```

Expand description

<div class="docblock">

A raw hash table with an unsafe API.

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-RawTable%3CT%3E" class="section impl">

<a href="../../src/hashbrown/raw/mod.rs.html#387-413"
class="src rightside">Source</a><a href="#impl-RawTable%3CT%3E" class="anchor">§</a>

### impl\<T\> <a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<T, Global\>

</div>

<div class="impl-items">

<div id="method.new" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#394-399"
class="src rightside">Source</a>

#### pub const fn <a href="#method.new" class="fn">new</a>() -\> Self

</div>

<div class="docblock">

Creates a new empty hash table without allocating any memory.

In effect this returns a table with exactly 1 bucket. However we can
leave the data pointer dangling since that bucket is never written to
due to our load factor forcing us to always have at least 1 free bucket.

</div>

<div id="method.try_with_capacity" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#404-406"
class="src rightside">Source</a>

#### pub fn <a href="#method.try_with_capacity" class="fn">try_with_capacity</a>(capacity: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<Self, <a href="../enum.TryReserveError.html" class="enum"
title="enum hashbrown::TryReserveError">TryReserveError</a>\>

</div>

<div class="docblock">

Attempts to allocate a new hash table with at least enough capacity for
inserting the given number of elements without reallocating.

</div>

<div id="method.with_capacity" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#410-412"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_capacity" class="fn">with_capacity</a>(capacity: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>) -\> Self

</div>

<div class="docblock">

Allocates a new hash table with at least enough capacity for inserting
the given number of elements without reallocating.

</div>

</div>

<div id="impl-RawTable%3CT,+A%3E" class="section impl">

<a href="../../src/hashbrown/raw/mod.rs.html#415-1026"
class="src rightside">Source</a><a href="#impl-RawTable%3CT,+A%3E" class="anchor">§</a>

### impl\<T, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<T, A\>

</div>

<div class="impl-items">

<div id="method.new_in" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#423-428"
class="src rightside">Source</a>

#### pub fn <a href="#method.new_in" class="fn">new_in</a>(alloc: A) -\> Self

</div>

<div class="docblock">

Creates a new empty hash table without allocating any memory, using the
given allocator.

In effect this returns a table with exactly 1 bucket. However we can
leave the data pointer dangling since that bucket is never written to
due to our load factor forcing us to always have at least 1 free bucket.

</div>

<div id="method.try_with_capacity_in" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#473-475"
class="src rightside">Source</a>

#### pub fn <a href="#method.try_with_capacity_in"
class="fn">try_with_capacity_in</a>( capacity: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>, alloc: A, ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<Self, <a href="../enum.TryReserveError.html" class="enum"
title="enum hashbrown::TryReserveError">TryReserveError</a>\>

</div>

<div class="docblock">

Attempts to allocate a new hash table using the given allocator, with at
least enough capacity for inserting the given number of elements without
reallocating.

</div>

<div id="method.with_capacity_in" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#479-485"
class="src rightside">Source</a>

#### pub fn <a href="#method.with_capacity_in" class="fn">with_capacity_in</a>(capacity: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>, alloc: A) -\> Self

</div>

<div class="docblock">

Allocates a new hash table using the given allocator, with at least
enough capacity for inserting the given number of elements without
reallocating.

</div>

<div id="method.allocator" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#489-491"
class="src rightside">Source</a>

#### pub fn <a href="#method.allocator" class="fn">allocator</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;A</a>

</div>

<div class="docblock">

Returns a reference to the underlying allocator.

</div>

<div id="method.data_end" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#501-503"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.data_end" class="fn">data_end</a>(&self) -\> <a
href="https://doc.rust-lang.org/1.92.0/core/ptr/non_null/struct.NonNull.html"
class="struct" title="struct core::ptr::non_null::NonNull">NonNull</a>\<T\>

</div>

<div class="docblock">

Returns pointer to one past last element of data table.

</div>

<div id="method.bucket_index" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#514-516"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.bucket_index" class="fn">bucket_index</a>(&self, bucket: &<a href="struct.Bucket.html" class="struct"
title="struct hashbrown::raw::Bucket">Bucket</a>\<T\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Returns the index of a bucket from a `Bucket`.

</div>

<div id="method.bucket" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#520-524"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.bucket" class="fn">bucket</a>(&self, index: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="struct.Bucket.html" class="struct"
title="struct hashbrown::raw::Bucket">Bucket</a>\<T\>

</div>

<div class="docblock">

Returns a pointer to an element in the table.

</div>

<div id="method.erase_no_drop" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#529-532"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.erase_no_drop" class="fn">erase_no_drop</a>(&mut self, item: &<a href="struct.Bucket.html" class="struct"
title="struct hashbrown::raw::Bucket">Bucket</a>\<T\>)

</div>

<span class="item-info"></span>

<div class="stab deprecated">

👎Deprecated since 0.8.1: use erase or remove instead

</div>

<div class="docblock">

Erases an element from the table without dropping it.

</div>

<div id="method.erase" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#538-542"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.erase" class="fn">erase</a>(&mut self, item: <a href="struct.Bucket.html" class="struct"
title="struct hashbrown::raw::Bucket">Bucket</a>\<T\>)

</div>

<div class="docblock">

Erases an element from the table, dropping it in place.

</div>

<div id="method.erase_entry" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#548-558"
class="src rightside">Source</a>

#### pub fn <a href="#method.erase_entry" class="fn">erase_entry</a>(&mut self, hash: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, eq: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Finds and erases an element from the table, dropping it in place.
Returns true if an element was found.

</div>

<div id="method.remove" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#564-567"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.remove" class="fn">remove</a>(&mut self, item: <a href="struct.Bucket.html" class="struct"
title="struct hashbrown::raw::Bucket">Bucket</a>\<T\>) -\> T

</div>

<div class="docblock">

Removes an element from the table, returning it.

</div>

<div id="method.remove_entry" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#571-577"
class="src rightside">Source</a>

#### pub fn <a href="#method.remove_entry" class="fn">remove_entry</a>( &mut self, hash: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, eq: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>, ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div class="docblock">

Finds and removes an element from the table, returning it.

</div>

<div id="method.clear_no_drop" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#581-583"
class="src rightside">Source</a>

#### pub fn <a href="#method.clear_no_drop" class="fn">clear_no_drop</a>(&mut self)

</div>

<div class="docblock">

Marks all table buckets as empty without dropping their contents.

</div>

<div id="method.clear" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#587-593"
class="src rightside">Source</a>

#### pub fn <a href="#method.clear" class="fn">clear</a>(&mut self)

</div>

<div class="docblock">

Removes all elements from the table without freeing the backing memory.

</div>

<div id="method.shrink_to" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#605-638"
class="src rightside">Source</a>

#### pub fn <a href="#method.shrink_to" class="fn">shrink_to</a>(&mut self, min_size: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>, hasher: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.Fn.html"
class="trait" title="trait core::ops::function::Fn">Fn</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>)

</div>

<div class="docblock">

Shrinks the table to fit `max(self.len(), min_size)` elements.

</div>

<div id="method.reserve" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#643-653"
class="src rightside">Source</a>

#### pub fn <a href="#method.reserve" class="fn">reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>, hasher: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.Fn.html"
class="trait" title="trait core::ops::function::Fn">Fn</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>)

</div>

<div class="docblock">

Ensures that at least `additional` items can be inserted into the table
without reallocation.

</div>

<div id="method.try_reserve" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#658-668"
class="src rightside">Source</a>

#### pub fn <a href="#method.try_reserve" class="fn">try_reserve</a>( &mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>, hasher: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.Fn.html"
class="trait" title="trait core::ops::function::Fn">Fn</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.unit.html"
class="primitive">()</a>, <a href="../enum.TryReserveError.html" class="enum"
title="enum hashbrown::TryReserveError">TryReserveError</a>\>

</div>

<div class="docblock">

Tries to ensure that at least `additional` items can be inserted into
the table without reallocation.

</div>

<div id="method.insert" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#716-735"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert" class="fn">insert</a>( &mut self, hash: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, value: T, hasher: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.Fn.html"
class="trait" title="trait core::ops::function::Fn">Fn</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, ) -\> <a href="struct.Bucket.html" class="struct"
title="struct hashbrown::raw::Bucket">Bucket</a>\<T\>

</div>

<div class="docblock">

Inserts a new element into the table, and returns its raw bucket.

This does not check if the given element already exists in the table.

</div>

<div id="method.try_insert_no_grow" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#745-756"
class="src rightside">Source</a>

#### pub fn <a href="#method.try_insert_no_grow" class="fn">try_insert_no_grow</a>( &mut self, hash: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, value: T, ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<<a href="struct.Bucket.html" class="struct"
title="struct hashbrown::raw::Bucket">Bucket</a>\<T\>, T\>

</div>

<div class="docblock">

Attempts to insert a new element without growing the table and return
its raw bucket.

Returns an `Err` containing the given element if inserting it would
require growing the table.

This does not check if the given element already exists in the table.

</div>

<div id="method.insert_entry" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#762-764"
class="src rightside">Source</a>

#### pub fn <a href="#method.insert_entry" class="fn">insert_entry</a>( &mut self, hash: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, value: T, hasher: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.Fn.html"
class="trait" title="trait core::ops::function::Fn">Fn</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut T</a>

</div>

<div class="docblock">

Inserts a new element into the table, and returns a mutable reference to
it.

This does not check if the given element already exists in the table.

</div>

<div id="method.insert_no_grow" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#773-784"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.insert_no_grow" class="fn">insert_no_grow</a>(&mut self, hash: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, value: T) -\> <a href="struct.Bucket.html" class="struct"
title="struct hashbrown::raw::Bucket">Bucket</a>\<T\>

</div>

<div class="docblock">

Inserts a new element into the table, without growing the table.

There must be enough space in the table to insert the new element.

This does not check if the given element already exists in the table.

</div>

<div id="method.replace_bucket_with" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#793-811"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.replace_bucket_with" class="fn">replace_bucket_with</a>\<F\>(&mut self, bucket: <a href="struct.Bucket.html" class="struct"
title="struct hashbrown::raw::Bucket">Bucket</a>\<T\>, f: F) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

<div class="where">

where F: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnOnce.html"
class="trait" title="trait core::ops::function::FnOnce">FnOnce</a>(T)
-\>
<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>,

</div>

</div>

<div class="docblock">

Temporary removes a bucket, applying the given function to the removed
element and optionally put back the returned value in the same bucket.

Returns `true` if the bucket still contains an element

This does not check if the given bucket is actually occupied.

</div>

<div id="method.find" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#815-825"
class="src rightside">Source</a>

#### pub fn <a href="#method.find" class="fn">find</a>(&self, hash: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, eq: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="struct.Bucket.html" class="struct"
title="struct hashbrown::raw::Bucket">Bucket</a>\<T\>\>

</div>

<div class="docblock">

Searches for an element in the table.

</div>

<div id="method.get" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#829-835"
class="src rightside">Source</a>

#### pub fn <a href="#method.get" class="fn">get</a>(&self, hash: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, eq: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>\>

</div>

<div class="docblock">

Gets a reference to an element in the table.

</div>

<div id="method.get_mut" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#839-845"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_mut" class="fn">get_mut</a>( &mut self, hash: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, eq: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>, ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut T</a>\>

</div>

<div class="docblock">

Gets a mutable reference to an element in the table.

</div>

<div id="method.get_many_mut" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#856-875"
class="src rightside">Source</a>

#### pub fn <a href="#method.get_many_mut" class="fn">get_many_mut</a>\<const N: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>\>( &mut self, hashes: \[<a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>; <a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\], eq: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>, ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<\[<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut T</a>; <a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\]\>

</div>

<div class="docblock">

Attempts to get mutable references to `N` entries in the table at once.

Returns an array of length `N` with the results of each query.

At most one mutable reference will be returned to any entry. `None` will
be returned if any of the hashes are duplicates. `None` will be returned
if the hash is not found.

The `eq` argument should be a closure such that `eq(i, k)` returns true
if `k` is equal to the `i`th key to be looked up.

</div>

<div id="method.get_many_unchecked_mut" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#877-884"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.get_many_unchecked_mut"
class="fn">get_many_unchecked_mut</a>\<const N: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>\>( &mut self, hashes: \[<a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>; <a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\], eq: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.FnMut.html"
class="trait" title="trait core::ops::function::FnMut">FnMut</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>, <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>, ) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<\[<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;mut T</a>; <a href="https://doc.rust-lang.org/1.92.0/core/primitive.array.html"
class="primitive">N</a>\]\>

</div>

<div id="method.capacity" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#909-911"
class="src rightside">Source</a>

#### pub fn <a href="#method.capacity" class="fn">capacity</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Returns the number of elements the map can hold without reallocating.

This number is a lower bound; the table might be able to hold more, but
is guaranteed to be able to hold at least this many.

</div>

<div id="method.len" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#915-917"
class="src rightside">Source</a>

#### pub fn <a href="#method.len" class="fn">len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Returns the number of elements in the table.

</div>

<div id="method.is_empty" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#921-923"
class="src rightside">Source</a>

#### pub fn <a href="#method.is_empty" class="fn">is_empty</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Returns `true` if the table contains no elements.

</div>

<div id="method.buckets" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#927-929"
class="src rightside">Source</a>

#### pub fn <a href="#method.buckets" class="fn">buckets</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

Returns the number of buckets in the table.

</div>

<div id="method.iter" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#936-942"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.iter" class="fn">iter</a>(&self) -\> <a href="struct.RawIter.html" class="struct"
title="struct hashbrown::raw::RawIter">RawIter</a>\<T\> <a href="#" class="tooltip" data-notable-ty="RawIter&lt;T&gt;">ⓘ</a>

</div>

<div class="docblock">

Returns an iterator over every element in the table. It is up to the
caller to ensure that the `RawTable` outlives the `RawIter`. Because we
cannot make the `next` method unsafe on the `RawIter` struct, we have to
make the `iter` method unsafe.

</div>

<div id="method.iter_hash" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#955-957"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.iter_hash" class="fn">iter_hash</a>(&self, hash: <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>) -\> <a href="struct.RawIterHash.html" class="struct"
title="struct hashbrown::raw::RawIterHash">RawIterHash</a>\<'\_, T, A\> <a href="#" class="tooltip"
data-notable-ty="RawIterHash&lt;&#39;_, T, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Returns an iterator over occupied buckets that could match a given hash.

`RawTable` only stores 7 bits of the hash value, so this iterator may
return items that have a hash value different than the one provided. You
should always validate the returned values before using them.

It is up to the caller to ensure that the `RawTable` outlives the
`RawIterHash`. Because we cannot make the `next` method unsafe on the
`RawIterHash` struct, we have to make the `iter_hash` method unsafe.

</div>

<div id="method.drain" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#962-967"
class="src rightside">Source</a>

#### pub fn <a href="#method.drain" class="fn">drain</a>(&mut self) -\> <a href="struct.RawDrain.html" class="struct"
title="struct hashbrown::raw::RawDrain">RawDrain</a>\<'\_, T, A\> <a href="#" class="tooltip"
data-notable-ty="RawDrain&lt;&#39;_, T, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Returns an iterator which removes all elements from the table without
freeing the memory.

</div>

<div id="method.drain_iter_from" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#977-985"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.drain_iter_from" class="fn">drain_iter_from</a>(&mut self, iter: <a href="struct.RawIter.html" class="struct"
title="struct hashbrown::raw::RawIter">RawIter</a>\<T\>) -\> <a href="struct.RawDrain.html" class="struct"
title="struct hashbrown::raw::RawDrain">RawDrain</a>\<'\_, T, A\> <a href="#" class="tooltip"
data-notable-ty="RawDrain&lt;&#39;_, T, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Returns an iterator which removes all elements from the table without
freeing the memory.

Iteration starts at the provided iterator’s current location.

It is up to the caller to ensure that the iterator is valid for this
`RawTable` and covers all items that remain in the table.

</div>

<div id="method.into_iter_from" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#993-1004"
class="src rightside">Source</a>

#### pub unsafe fn <a href="#method.into_iter_from" class="fn">into_iter_from</a>(self, iter: <a href="struct.RawIter.html" class="struct"
title="struct hashbrown::raw::RawIter">RawIter</a>\<T\>) -\> <a href="struct.RawIntoIter.html" class="struct"
title="struct hashbrown::raw::RawIntoIter">RawIntoIter</a>\<T, A\> <a href="#" class="tooltip"
data-notable-ty="RawIntoIter&lt;T, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Returns an iterator which consumes all elements from the table.

Iteration starts at the provided iterator’s current location.

It is up to the caller to ensure that the iterator is valid for this
`RawTable` and covers all items that remain in the table.

</div>

</div>

<div id="impl-RawTable%3CT,+A%3E-1" class="section impl">

<a href="../../src/hashbrown/raw/mod.rs.html#1706-1791"
class="src rightside">Source</a><a href="#impl-RawTable%3CT,+A%3E-1" class="anchor">§</a>

### impl\<T: <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<T, A\>

</div>

<div class="impl-items">

<div id="method.clone_from_with_hasher" class="section method">

<a href="../../src/hashbrown/raw/mod.rs.html#1750-1790"
class="src rightside">Source</a>

#### pub fn <a href="#method.clone_from_with_hasher"
class="fn">clone_from_with_hasher</a>( &mut self, source: &Self, hasher: impl <a
href="https://doc.rust-lang.org/1.92.0/core/ops/function/trait.Fn.html"
class="trait" title="trait core::ops::function::Fn">Fn</a>(<a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;T</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>, )

</div>

<div class="docblock">

Variant of `clone_from` to use when a hasher is available.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-RawTable%3CT,+A%3E" class="section impl">

<a href="../../src/hashbrown/raw/mod.rs.html#1599-1675"
class="src rightside">Source</a><a href="#impl-Clone-for-RawTable%3CT,+A%3E" class="anchor">§</a>

### impl\<T: <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<T, A\>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../../src/hashbrown/raw/mod.rs.html#1600-1628"
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

<a href="../../src/hashbrown/raw/mod.rs.html#1630-1674"
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

<div id="impl-Default-for-RawTable%3CT,+A%3E" class="section impl">

<a href="../../src/hashbrown/raw/mod.rs.html#1793-1798"
class="src rightside">Source</a><a href="#impl-Default-for-RawTable%3CT,+A%3E" class="anchor">§</a>

### impl\<T, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> + <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>\> <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a> for <a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<T, A\>

</div>

<div class="impl-items">

<div id="method.default" class="section method trait-impl">

<a href="../../src/hashbrown/raw/mod.rs.html#1795-1797"
class="src rightside">Source</a><a href="#method.default" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html#tymethod.default"
class="fn">default</a>() -\> Self

</div>

<div class="docblock">

Returns the “default value” for a type. [Read
more](https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html#tymethod.default)

</div>

</div>

<div id="impl-Drop-for-RawTable%3CT,+A%3E" class="section impl">

<a href="../../src/hashbrown/raw/mod.rs.html#1813-1823"
class="src rightside">Source</a><a href="#impl-Drop-for-RawTable%3CT,+A%3E" class="anchor">§</a>

### impl\<T, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a href="https://doc.rust-lang.org/1.92.0/core/ops/drop/trait.Drop.html"
class="trait" title="trait core::ops::drop::Drop">Drop</a> for <a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<T, A\>

<span class="item-info"></span>

<div class="stab portability">

Available on **non-crate feature `nightly`** only.

</div>

</div>

<div class="impl-items">

<div id="method.drop" class="section method trait-impl">

<a href="../../src/hashbrown/raw/mod.rs.html#1815-1822"
class="src rightside">Source</a><a href="#method.drop" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/drop/trait.Drop.html#tymethod.drop"
class="fn">drop</a>(&mut self)

</div>

<div class="docblock">

Executes the destructor for this type. [Read
more](https://doc.rust-lang.org/1.92.0/core/ops/drop/trait.Drop.html#tymethod.drop)

</div>

</div>

<div id="impl-IntoIterator-for-RawTable%3CT,+A%3E" class="section impl">

<a href="../../src/hashbrown/raw/mod.rs.html#1825-1836"
class="src rightside">Source</a><a href="#impl-IntoIterator-for-RawTable%3CT,+A%3E" class="anchor">§</a>

### impl\<T, A: Allocator + <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a> for <a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<T, A\>

</div>

<div class="impl-items">

<div id="associatedtype.Item" class="section associatedtype trait-impl">

<a href="../../src/hashbrown/raw/mod.rs.html#1826"
class="src rightside">Source</a><a href="#associatedtype.Item" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype">Item</a> = T

</div>

<div class="docblock">

The type of the elements being iterated over.

</div>

<div id="associatedtype.IntoIter"
class="section associatedtype trait-impl">

<a href="../../src/hashbrown/raw/mod.rs.html#1827"
class="src rightside">Source</a><a href="#associatedtype.IntoIter" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.IntoIter"
class="associatedtype">IntoIter</a> = <a href="struct.RawIntoIter.html" class="struct"
title="struct hashbrown::raw::RawIntoIter">RawIntoIter</a>\<T, A\>

</div>

<div class="docblock">

Which kind of iterator are we turning this into?

</div>

<div id="method.into_iter" class="section method trait-impl">

<a href="../../src/hashbrown/raw/mod.rs.html#1830-1835"
class="src rightside">Source</a><a href="#method.into_iter" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter"
class="fn">into_iter</a>(self) -\> <a href="struct.RawIntoIter.html" class="struct"
title="struct hashbrown::raw::RawIntoIter">RawIntoIter</a>\<T, A\> <a href="#" class="tooltip"
data-notable-ty="RawIntoIter&lt;T, A&gt;">ⓘ</a>

</div>

<div class="docblock">

Creates an iterator from a value. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#tymethod.into_iter)

</div>

</div>

<div id="impl-Send-for-RawTable%3CT,+A%3E" class="section impl">

<a href="../../src/hashbrown/raw/mod.rs.html#1028-1033"
class="src rightside">Source</a><a href="#impl-Send-for-RawTable%3CT,+A%3E" class="anchor">§</a>

### impl\<T, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<T, A\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> + Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div id="impl-Sync-for-RawTable%3CT,+A%3E" class="section impl">

<a href="../../src/hashbrown/raw/mod.rs.html#1034-1039"
class="src rightside">Source</a><a href="#impl-Sync-for-RawTable%3CT,+A%3E" class="anchor">§</a>

### impl\<T, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<T, A\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> + Allocator +
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-RawTable%3CT,+A%3E" class="section impl">

<a href="#impl-Freeze-for-RawTable%3CT,+A%3E" class="anchor">§</a>

### impl\<T, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<T, A\>

<div class="where">

where A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>,

</div>

</div>

<div id="impl-RefUnwindSafe-for-RawTable%3CT,+A%3E"
class="section impl">

<a href="#impl-RefUnwindSafe-for-RawTable%3CT,+A%3E"
class="anchor">§</a>

### impl\<T, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<T, A\>

<div class="where">

where A: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
T: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

<div id="impl-Unpin-for-RawTable%3CT,+A%3E" class="section impl">

<a href="#impl-Unpin-for-RawTable%3CT,+A%3E" class="anchor">§</a>

### impl\<T, A\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<T, A\>

<div class="where">

where A:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-RawTable%3CT,+A%3E" class="section impl">

<a href="#impl-UnwindSafe-for-RawTable%3CT,+A%3E" class="anchor">§</a>

### impl\<T, A\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.RawTable.html" class="struct"
title="struct hashbrown::raw::RawTable">RawTable</a>\<T, A\>

<div class="where">

where A: <a
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
