<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)

</div>

# Module simple_pptr Copy item path

<span class="sub-heading"><a href="../../src/vstd/simple_pptr.rs.html#1-559"
class="src">Source</a> </span>

</div>

## Re-exports<a href="#reexports" class="anchor">§</a>

`pub use raw_ptr::`<a href="../raw_ptr/enum.MemContents.html" class="enum"
title="enum vstd::raw_ptr::MemContents"><code>MemContents</code></a>`;`

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.PPtr.html" class="struct"
title="struct vstd::simple_pptr::PPtr">PPtr</a>  
`PPtr` (which stands for “permissioned pointer”) is a wrapper around a
raw pointer to a heap-allocated `V`. This is designed to be simpler to
use that Verus’s [more general pointer
support](../raw_ptr/index.html "mod vstd::raw_ptr"), but also to serve
as a better introductory point. Historically, `PPtr` was positioned as a
“trusted primitive” of Verus, but now, it is implemented and verified
from the more general pointer support, which operates on similar
principles, but which is much precise to Rust’s pointer semantics.

<a href="struct.PointsTo.html" class="struct"
title="struct vstd::simple_pptr::PointsTo">PointsTo</a>  
A `tracked` ghost object that gives the user permission to dereference a
pointer for reading or writing, or to free the memory at that pointer.

</div>

</div>
