<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)

</div>

# Module raw_ptr Copy item path

<span class="sub-heading"><a href="../../src/vstd/raw_ptr.rs.html#1-1011" class="src">Source</a>
</span>

</div>

Expand description

<div class="docblock">

Tools and reasoning principles for [raw
pointers](https://doc.rust-lang.org/std/primitive.pointer.html). The
tools here are meant to address “real Rust pointers, including all their
subtleties on the Rust Abstract Machine, to the largest extent that is
reasonable.”

For a gentler introduction to some of the concepts here, see
[`PPtr`](../simple_pptr/index.html "mod vstd::simple_pptr"), which uses
a much-simplified pointer model.

#### <a href="#pointer-model" class="doc-anchor">§</a>Pointer model

A pointer consists of an address (`ptr.addr()` or `ptr as usize`), a
provenance `ptr@.provenance`, and metadata `ptr@.metadata` (which is
trivial except for pointers to non-sized types). Note that in spec code,
pointer equality requires *all 3* to be equal, whereas runtime equality
(eq) only compares addresses and metadata.

`*mut T` vs. `*const T` do not have any semantic difference and Verus
treats them as the same; they can be seamlessly cast to and fro.

</div>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.Dealloc.html" class="struct"
title="struct vstd::raw_ptr::Dealloc">Dealloc</a>  
Permission to perform a deallocation with the global allocator.

<a href="struct.DeallocData.html" class="struct"
title="struct vstd::raw_ptr::DeallocData">DeallocData</a>  
Data associated with a `Dealloc` permission.

<a href="struct.FakeMetadata.html" class="struct"
title="struct vstd::raw_ptr::FakeMetadata">FakeMetadata</a>  
<a href="struct.IsExposed.html" class="struct"
title="struct vstd::raw_ptr::IsExposed">IsExposed</a>  
Tracked object that indicates a given provenance has been exposed.

<a href="struct.PointsTo.html" class="struct"
title="struct vstd::raw_ptr::PointsTo">PointsTo</a>  
Permission to access possibly-initialized, *typed* memory.

<a href="struct.PointsToData.html" class="struct"
title="struct vstd::raw_ptr::PointsToData">PointsToData</a>  
Data associated with a `PointsTo` permission. We keep track of both the
pointer and the (potentially uninitialized) value it points to.

<a href="struct.PointsToRaw.html" class="struct"
title="struct vstd::raw_ptr::PointsToRaw">PointsToRaw</a>  
Variable-sized uninitialized memory.

<a href="struct.Provenance.html" class="struct"
title="struct vstd::raw_ptr::Provenance">Provenance</a>  
Provenance

<a href="struct.SharedReference.html" class="struct"
title="struct vstd::raw_ptr::SharedReference">SharedReference</a>  
This is meant to be a replacement for `&'a T` that allows Verus to keep
track of not just the `T` value but the pointer as well. It would be
better to get rid of this and use normal reference types `&'a T`, but
there are a lot of unsolved implementation questions. The existence of
`SharedReference<'a, T>` is a stop-gap.

## Enums<a href="#enums" class="anchor">§</a>

<a href="enum.MemContents.html" class="enum"
title="enum vstd::raw_ptr::MemContents">MemContents</a>  
Represents (typed) contents of memory.

## Functions<a href="#functions" class="anchor">§</a>

<a href="fn.allocate.html" class="fn"
title="fn vstd::raw_ptr::allocate">allocate</a>  
Allocate with the global allocator. The precondition should be
consistent with the [documented safety conditions on
`alloc`](https://doc.rust-lang.org/alloc/alloc/trait.GlobalAlloc.html#tymethod.alloc).
Returns a pointer with a corresponding
[`PointsToRaw`](struct.PointsToRaw.html "struct vstd::raw_ptr::PointsToRaw")
and [`Dealloc`](struct.Dealloc.html "struct vstd::raw_ptr::Dealloc")
permissions.

<a href="fn.cast_array_ptr_to_slice_ptr.html" class="fn"
title="fn vstd::raw_ptr::cast_array_ptr_to_slice_ptr">cast_array_ptr_to_slice_ptr</a>  
Cast a pointer to an array of length `N` to a slice pointer. Address and
provenance are preserved; metadata has length `N`.

<a href="fn.cast_ptr_to_thin_ptr.html" class="fn"
title="fn vstd::raw_ptr::cast_ptr_to_thin_ptr">cast_ptr_to_thin_ptr</a>  
Cast a pointer to a thin pointer. Address and provenance are preserved;
metadata is now thin.

<a href="fn.cast_ptr_to_usize.html" class="fn"
title="fn vstd::raw_ptr::cast_ptr_to_usize">cast_ptr_to_usize</a>  
Cast the address of a pointer to a `usize`.

<a href="fn.cast_slice_ptr_to_slice_ptr.html" class="fn"
title="fn vstd::raw_ptr::cast_slice_ptr_to_slice_ptr">cast_slice_ptr_to_slice_ptr</a>  
Cast a slice pointer to another slice pointer. Length is preserved even
if the size of the elements changes.

<a href="fn.cast_slice_ptr_to_str_ptr.html" class="fn"
title="fn vstd::raw_ptr::cast_slice_ptr_to_str_ptr">cast_slice_ptr_to_str_ptr</a>  
Cast a slice pointer to a `str` pointer. Length is preserved even if the
size of the elements changes.

<a href="fn.cast_str_ptr_to_slice_ptr.html" class="fn"
title="fn vstd::raw_ptr::cast_str_ptr_to_slice_ptr">cast_str_ptr_to_slice_ptr</a>  
Cast a `str` pointer to a slice pointer. Length is preserved even if the
size of the elements changes.

<a href="fn.deallocate.html" class="fn"
title="fn vstd::raw_ptr::deallocate">deallocate</a>  
Deallocate with the global allocator.

<a href="fn.expose_provenance.html" class="fn"
title="fn vstd::raw_ptr::expose_provenance">expose_provenance</a>  
Perform a provenance expose operation.

<a href="fn.group_raw_ptr_axioms.html" class="fn"
title="fn vstd::raw_ptr::group_raw_ptr_axioms">group_raw_ptr_axioms</a>  
<a href="fn.ptr_mut_read.html" class="fn"
title="fn vstd::raw_ptr::ptr_mut_read">ptr_mut_read</a>  
Calls
[`core::ptr::read`](https://doc.rust-lang.org/1.92.0/core/ptr/fn.read.html "fn core::ptr::read")
to read from the memory pointed to by `ptr`, using the permission
`perm`.

<a href="fn.ptr_mut_write.html" class="fn"
title="fn vstd::raw_ptr::ptr_mut_write">ptr_mut_write</a>  
Calls
[`core::ptr::write`](https://doc.rust-lang.org/1.92.0/core/ptr/fn.write.html "fn core::ptr::write")
to write the value `v` to the memory location pointed to by `ptr`, using
the permission `perm`.

<a href="fn.ptr_ref.html" class="fn"
title="fn vstd::raw_ptr::ptr_ref">ptr_ref</a>  
Equivalent to `&*ptr`, passing in a permission `perm` to ensure safety.
The memory pointed to by `ptr` must be initialized.

<a href="fn.ptr_ref2.html" class="fn"
title="fn vstd::raw_ptr::ptr_ref2">ptr_ref2</a>  
Like [`ptr_ref`](fn.ptr_ref.html "fn vstd::raw_ptr::ptr_ref") but
returns a `SharedReference` so it keeps track of the relationship
between the pointers. Note the resulting reference’s pointers does NOT
have the same provenance. This is because in Rust models like Stacked
Borrows / Tree Borrows, the pointer gets a new tag.

<a href="fn.with_exposed_provenance.html" class="fn"
title="fn vstd::raw_ptr::with_exposed_provenance">with_exposed_provenance</a>  
Construct a pointer with the given provenance from a *usize* address.
The provenance must have previously been exposed.

## Type Aliases<a href="#types" class="anchor">§</a>

<a href="type.Metadata.html" class="type"
title="type vstd::raw_ptr::Metadata">Metadata</a>

</div>

</div>
