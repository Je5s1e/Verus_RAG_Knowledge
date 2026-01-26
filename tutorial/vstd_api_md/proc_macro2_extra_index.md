<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[proc_macro2](../index.html)

</div>

# Module extra Copy item path

<span class="sub-heading"><a href="../../src/proc_macro2/extra.rs.html#1-151"
class="src">Source</a> </span>

</div>

Expand description

<div class="docblock">

Items which do not have a correspondence to any API in the proc_macro
crate, but are necessary to include in proc-macro2.

</div>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.DelimSpan.html" class="struct"
title="struct proc_macro2::extra::DelimSpan">DelimSpan</a>  
An object that holds a
[`Group`](../struct.Group.html "struct proc_macro2::Group")’s
`span_open()` and `span_close()` together in a more compact
representation than holding those 2 spans individually.

## Functions<a href="#functions" class="anchor">§</a>

<a href="fn.invalidate_current_thread_spans.html" class="fn"
title="fn proc_macro2::extra::invalidate_current_thread_spans">invalidate_current_thread_spans</a>  
Invalidate any `proc_macro2::Span` that exist on the current thread.

</div>

</div>
