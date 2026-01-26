<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)

</div>

# Module contrib Copy item path

<span class="sub-heading"><a href="../../src/vstd/contrib/mod.rs.html#1-2" class="src">Source</a>
</span>

</div>

## Modules<a href="#modules" class="anchor">§</a>

<a href="exec_spec/index.html" class="mod"
title="mod vstd::contrib::exec_spec">exec_spec</a>  
This module provides runtime utilities for the compiled executable code
of
[`verus_builtin_macros::exec_spec`](exec_spec/macro.exec_spec.html "macro vstd::contrib::exec_spec::exec_spec").

## Attribute Macros<a href="#attributes" class="anchor">§</a>

<a href="attr.auto_spec.html" class="attr"
title="attr vstd::contrib::auto_spec">auto_spec</a>  
This copies the body of an exec function into a “returns” clause, so
that the exec function will be also usable as a spec function. For
example, `#[vstd::contrib::auto_spec] fn f(u: u8) -> u8 { u / 2 }`
becomes:
`#[verifier::allow_in_spec] fn f(u: u8) -> u8 returns (u / 2) { u / 2 }`
The macro performs some limited fixups, such as removing proof blocks
and turning +, -, and \* into add, sub, mul. However, only a few such
fixups are currently implemented and not all exec bodies will be usable
as return clauses, so this macro will not work on all exec functions.

</div>

</div>
