<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[invariant](index.html)

</div>

# Trait <span class="trait">InvariantPredicate</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/invariant.rs.html#54-56" class="src">Source</a>
</span>

</div>

``` rust
pub trait InvariantPredicate<K, V> { }
```

Expand description

<div class="docblock">

Trait used to specify an *invariant predicate* for
[`LocalInvariant`](struct.LocalInvariant.html "struct vstd::invariant::LocalInvariant")
and
[`AtomicInvariant`](struct.AtomicInvariant.html "struct vstd::invariant::AtomicInvariant").

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-InvariantPredicate%3C(K,+int),+(PermissionBool,+G)%3E-for-AtomicPredBool%3CPred%3E"
class="section impl">

<a href="../../src/vstd/atomic_ghost.rs.html#210"
class="src rightside">Source</a><a
href="#impl-InvariantPredicate%3C(K,+int),+(PermissionBool,+G)%3E-for-AtomicPredBool%3CPred%3E"
class="anchor">§</a>

### impl\<K, G, Pred\> <a href="trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<(K, <a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>), (<a href="../atomic/struct.PermissionBool.html" class="struct"
title="struct vstd::atomic::PermissionBool">PermissionBool</a>, G)\> for <a href="../atomic_ghost/struct.AtomicPredBool.html" class="struct"
title="struct vstd::atomic_ghost::AtomicPredBool">AtomicPredBool</a>\<Pred\>

<div class="where">

where Pred:
<a href="../atomic_ghost/trait.AtomicInvariantPredicate.html"
class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<K,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>, G\>,

</div>

</div>

<div id="impl-InvariantPredicate%3C(K,+int),+(PermissionI8,+G)%3E-for-AtomicPredI8%3CPred%3E"
class="section impl">

<a href="../../src/vstd/atomic_ghost.rs.html#207"
class="src rightside">Source</a><a
href="#impl-InvariantPredicate%3C(K,+int),+(PermissionI8,+G)%3E-for-AtomicPredI8%3CPred%3E"
class="anchor">§</a>

### impl\<K, G, Pred\> <a href="trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<(K, <a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>), (<a href="../atomic/struct.PermissionI8.html" class="struct"
title="struct vstd::atomic::PermissionI8">PermissionI8</a>, G)\> for <a href="../atomic_ghost/struct.AtomicPredI8.html" class="struct"
title="struct vstd::atomic_ghost::AtomicPredI8">AtomicPredI8</a>\<Pred\>

<div class="where">

where Pred:
<a href="../atomic_ghost/trait.AtomicInvariantPredicate.html"
class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<K,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>, G\>,

</div>

</div>

<div id="impl-InvariantPredicate%3C(K,+int),+(PermissionI16,+G)%3E-for-AtomicPredI16%3CPred%3E"
class="section impl">

<a href="../../src/vstd/atomic_ghost.rs.html#206"
class="src rightside">Source</a><a
href="#impl-InvariantPredicate%3C(K,+int),+(PermissionI16,+G)%3E-for-AtomicPredI16%3CPred%3E"
class="anchor">§</a>

### impl\<K, G, Pred\> <a href="trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<(K, <a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>), (<a href="../atomic/struct.PermissionI16.html" class="struct"
title="struct vstd::atomic::PermissionI16">PermissionI16</a>, G)\> for <a href="../atomic_ghost/struct.AtomicPredI16.html" class="struct"
title="struct vstd::atomic_ghost::AtomicPredI16">AtomicPredI16</a>\<Pred\>

<div class="where">

where Pred:
<a href="../atomic_ghost/trait.AtomicInvariantPredicate.html"
class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<K,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>, G\>,

</div>

</div>

<div id="impl-InvariantPredicate%3C(K,+int),+(PermissionI32,+G)%3E-for-AtomicPredI32%3CPred%3E"
class="section impl">

<a href="../../src/vstd/atomic_ghost.rs.html#205"
class="src rightside">Source</a><a
href="#impl-InvariantPredicate%3C(K,+int),+(PermissionI32,+G)%3E-for-AtomicPredI32%3CPred%3E"
class="anchor">§</a>

### impl\<K, G, Pred\> <a href="trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<(K, <a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>), (<a href="../atomic/struct.PermissionI32.html" class="struct"
title="struct vstd::atomic::PermissionI32">PermissionI32</a>, G)\> for <a href="../atomic_ghost/struct.AtomicPredI32.html" class="struct"
title="struct vstd::atomic_ghost::AtomicPredI32">AtomicPredI32</a>\<Pred\>

<div class="where">

where Pred:
<a href="../atomic_ghost/trait.AtomicInvariantPredicate.html"
class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<K,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>, G\>,

</div>

</div>

<div id="impl-InvariantPredicate%3C(K,+int),+(PermissionI64,+G)%3E-for-AtomicPredI64%3CPred%3E"
class="section impl">

<a href="../../src/vstd/atomic_ghost.rs.html#203"
class="src rightside">Source</a><a
href="#impl-InvariantPredicate%3C(K,+int),+(PermissionI64,+G)%3E-for-AtomicPredI64%3CPred%3E"
class="anchor">§</a>

### impl\<K, G, Pred\> <a href="trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<(K, <a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>), (<a href="../atomic/struct.PermissionI64.html" class="struct"
title="struct vstd::atomic::PermissionI64">PermissionI64</a>, G)\> for <a href="../atomic_ghost/struct.AtomicPredI64.html" class="struct"
title="struct vstd::atomic_ghost::AtomicPredI64">AtomicPredI64</a>\<Pred\>

<div class="where">

where Pred:
<a href="../atomic_ghost/trait.AtomicInvariantPredicate.html"
class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<K,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>, G\>,

</div>

</div>

<div id="impl-InvariantPredicate%3C(K,+int),+(PermissionIsize,+G)%3E-for-AtomicPredIsize%3CPred%3E"
class="section impl">

<a href="../../src/vstd/atomic_ghost.rs.html#208"
class="src rightside">Source</a><a
href="#impl-InvariantPredicate%3C(K,+int),+(PermissionIsize,+G)%3E-for-AtomicPredIsize%3CPred%3E"
class="anchor">§</a>

### impl\<K, G, Pred\> <a href="trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<(K, <a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>), (<a href="../atomic/struct.PermissionIsize.html" class="struct"
title="struct vstd::atomic::PermissionIsize">PermissionIsize</a>, G)\> for <a href="../atomic_ghost/struct.AtomicPredIsize.html" class="struct"
title="struct vstd::atomic_ghost::AtomicPredIsize">AtomicPredIsize</a>\<Pred\>

<div class="where">

where Pred:
<a href="../atomic_ghost/trait.AtomicInvariantPredicate.html"
class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<K,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>, G\>,

</div>

</div>

<div id="impl-InvariantPredicate%3C(K,+int),+(PermissionU8,+G)%3E-for-AtomicPredU8%3CPred%3E"
class="section impl">

<a href="../../src/vstd/atomic_ghost.rs.html#199"
class="src rightside">Source</a><a
href="#impl-InvariantPredicate%3C(K,+int),+(PermissionU8,+G)%3E-for-AtomicPredU8%3CPred%3E"
class="anchor">§</a>

### impl\<K, G, Pred\> <a href="trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<(K, <a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>), (<a href="../atomic/struct.PermissionU8.html" class="struct"
title="struct vstd::atomic::PermissionU8">PermissionU8</a>, G)\> for <a href="../atomic_ghost/struct.AtomicPredU8.html" class="struct"
title="struct vstd::atomic_ghost::AtomicPredU8">AtomicPredU8</a>\<Pred\>

<div class="where">

where Pred:
<a href="../atomic_ghost/trait.AtomicInvariantPredicate.html"
class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<K,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>, G\>,

</div>

</div>

<div id="impl-InvariantPredicate%3C(K,+int),+(PermissionU16,+G)%3E-for-AtomicPredU16%3CPred%3E"
class="section impl">

<a href="../../src/vstd/atomic_ghost.rs.html#198"
class="src rightside">Source</a><a
href="#impl-InvariantPredicate%3C(K,+int),+(PermissionU16,+G)%3E-for-AtomicPredU16%3CPred%3E"
class="anchor">§</a>

### impl\<K, G, Pred\> <a href="trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<(K, <a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>), (<a href="../atomic/struct.PermissionU16.html" class="struct"
title="struct vstd::atomic::PermissionU16">PermissionU16</a>, G)\> for <a href="../atomic_ghost/struct.AtomicPredU16.html" class="struct"
title="struct vstd::atomic_ghost::AtomicPredU16">AtomicPredU16</a>\<Pred\>

<div class="where">

where Pred:
<a href="../atomic_ghost/trait.AtomicInvariantPredicate.html"
class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<K,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>, G\>,

</div>

</div>

<div id="impl-InvariantPredicate%3C(K,+int),+(PermissionU32,+G)%3E-for-AtomicPredU32%3CPred%3E"
class="section impl">

<a href="../../src/vstd/atomic_ghost.rs.html#197"
class="src rightside">Source</a><a
href="#impl-InvariantPredicate%3C(K,+int),+(PermissionU32,+G)%3E-for-AtomicPredU32%3CPred%3E"
class="anchor">§</a>

### impl\<K, G, Pred\> <a href="trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<(K, <a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>), (<a href="../atomic/struct.PermissionU32.html" class="struct"
title="struct vstd::atomic::PermissionU32">PermissionU32</a>, G)\> for <a href="../atomic_ghost/struct.AtomicPredU32.html" class="struct"
title="struct vstd::atomic_ghost::AtomicPredU32">AtomicPredU32</a>\<Pred\>

<div class="where">

where Pred:
<a href="../atomic_ghost/trait.AtomicInvariantPredicate.html"
class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<K,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>, G\>,

</div>

</div>

<div id="impl-InvariantPredicate%3C(K,+int),+(PermissionU64,+G)%3E-for-AtomicPredU64%3CPred%3E"
class="section impl">

<a href="../../src/vstd/atomic_ghost.rs.html#195"
class="src rightside">Source</a><a
href="#impl-InvariantPredicate%3C(K,+int),+(PermissionU64,+G)%3E-for-AtomicPredU64%3CPred%3E"
class="anchor">§</a>

### impl\<K, G, Pred\> <a href="trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<(K, <a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>), (<a href="../atomic/struct.PermissionU64.html" class="struct"
title="struct vstd::atomic::PermissionU64">PermissionU64</a>, G)\> for <a href="../atomic_ghost/struct.AtomicPredU64.html" class="struct"
title="struct vstd::atomic_ghost::AtomicPredU64">AtomicPredU64</a>\<Pred\>

<div class="where">

where Pred:
<a href="../atomic_ghost/trait.AtomicInvariantPredicate.html"
class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<K,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>, G\>,

</div>

</div>

<div id="impl-InvariantPredicate%3C(K,+int),+(PermissionUsize,+G)%3E-for-AtomicPredUsize%3CPred%3E"
class="section impl">

<a href="../../src/vstd/atomic_ghost.rs.html#200"
class="src rightside">Source</a><a
href="#impl-InvariantPredicate%3C(K,+int),+(PermissionUsize,+G)%3E-for-AtomicPredUsize%3CPred%3E"
class="anchor">§</a>

### impl\<K, G, Pred\> <a href="trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<(K, <a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>), (<a href="../atomic/struct.PermissionUsize.html" class="struct"
title="struct vstd::atomic::PermissionUsize">PermissionUsize</a>, G)\> for <a href="../atomic_ghost/struct.AtomicPredUsize.html" class="struct"
title="struct vstd::atomic_ghost::AtomicPredUsize">AtomicPredUsize</a>\<Pred\>

<div class="where">

where Pred:
<a href="../atomic_ghost/trait.AtomicInvariantPredicate.html"
class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<K,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, G\>,

</div>

</div>

<div id="impl-InvariantPredicate%3C(K,+int),+(PermissionPtr%3CT%3E,+G)%3E-for-AtomicPredPtr%3CT,+Pred%3E"
class="section impl">

<a href="../../src/vstd/atomic_ghost.rs.html#212"
class="src rightside">Source</a><a
href="#impl-InvariantPredicate%3C(K,+int),+(PermissionPtr%3CT%3E,+G)%3E-for-AtomicPredPtr%3CT,+Pred%3E"
class="anchor">§</a>

### impl\<T, K, G, Pred\> <a href="trait.InvariantPredicate.html" class="trait"
title="trait vstd::invariant::InvariantPredicate">InvariantPredicate</a>\<(K, <a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>), (<a href="../atomic/struct.PermissionPtr.html" class="struct"
title="struct vstd::atomic::PermissionPtr">PermissionPtr</a>\<T\>, G)\> for <a href="../atomic_ghost/struct.AtomicPredPtr.html" class="struct"
title="struct vstd::atomic_ghost::AtomicPredPtr">AtomicPredPtr</a>\<T, Pred\>

<div class="where">

where Pred:
<a href="../atomic_ghost/trait.AtomicInvariantPredicate.html"
class="trait"
title="trait vstd::atomic_ghost::AtomicInvariantPredicate">AtomicInvariantPredicate</a>\<K,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.pointer.html"
class="primitive">*mut T</a>, G\>,

</div>

</div>

</div>

</div>

</div>
