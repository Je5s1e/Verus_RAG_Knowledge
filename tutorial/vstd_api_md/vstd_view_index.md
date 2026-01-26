<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)

</div>

# Module view Copy item path

<span class="sub-heading"><a href="../../src/vstd/view.rs.html#1-251" class="src">Source</a>
</span>

</div>

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>  
<a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>  
Types used in executable code can implement View to provide a
mathematical abstraction of the type. For example, Vec implements a view
method that returns a Seq. For base types like bool and u8, the view V
of the type is the type itself. Types only used in ghost code, such as
int, nat, and Seq, do not need to implement View.

</div>

</div>
