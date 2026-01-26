<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../../index.html)::[contrib](../index.html)

</div>

# Module exec_spec Copy item path

<span class="sub-heading"><a href="../../../src/vstd/contrib/exec_spec.rs.html#1-358"
class="src">Source</a> </span>

</div>

Expand description

<div class="docblock">

This module provides runtime utilities for the compiled executable code
of
[`verus_builtin_macros::exec_spec`](macro.exec_spec.html "macro vstd::contrib::exec_spec::exec_spec").

</div>

## Macros<a href="#macros" class="anchor">§</a>

<a href="macro.exec_spec.html" class="macro"
title="macro vstd::contrib::exec_spec::exec_spec">exec_spec</a>  
Automatically compiles spec items to exec items, with proofs of
functional correctness.

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a>  
Cloned objects have the same deep view

<a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>  
Spec for the executable version of equality.

<a href="trait.ExecSpecIndex.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecIndex">ExecSpecIndex</a>  
Spec for executable version of
[`Seq`](../../seq/struct.Seq.html "struct vstd::seq::Seq") indexing.

<a href="trait.ExecSpecLen.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecLen">ExecSpecLen</a>  
Spec for executable version of \[`Seq::len`\].

<a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a>  
Any spec types used in
[`exec_spec`](macro.exec_spec.html "macro vstd::contrib::exec_spec::exec_spec")
macro must implement this trait to indicate the corresponding exec type
(owned and borrowed versions).

<a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>  
<a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>  
[`ToRef`](trait.ToRef.html "trait vstd::contrib::exec_spec::ToRef") and
[`ToOwned`](trait.ToOwned.html "trait vstd::contrib::exec_spec::ToOwned")
are almost the same trait but separated to avoid type inference
ambiguities.

## Type Aliases<a href="#types" class="anchor">§</a>

<a href="type.SpecString.html" class="type"
title="type vstd::contrib::exec_spec::SpecString">SpecString</a>  
We use this special alias to tell the `exec_spec` macro to compile
[`Seq<char>`](../../seq/struct.Seq.html "struct vstd::seq::Seq") to
[`String`](https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html "struct alloc::string::String")
instead of
[`Vec<char>`](https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html "struct alloc::vec::Vec").

</div>

</div>
