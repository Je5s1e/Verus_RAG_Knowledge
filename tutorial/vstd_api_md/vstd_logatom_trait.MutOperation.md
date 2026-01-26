<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[logatom](index.html)

</div>

# Trait <span class="trait">MutOperation</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/logatom.rs.html#25-58" class="src">Source</a>
</span>

</div>

``` rust
pub trait MutOperation: Sized {
    type Resource;
    type ExecResult;
    type NewState;
}
```

## Required Associated Types<a href="#required-associated-types" class="anchor">§</a>

<div class="methods">

<div id="associatedtype.Resource" class="section method">

<a href="../../src/vstd/logatom.rs.html#27"
class="src rightside">Source</a>

#### type <a href="#associatedtype.Resource" class="associatedtype">Resource</a>

</div>

<div id="associatedtype.ExecResult" class="section method">

<a href="../../src/vstd/logatom.rs.html#30"
class="src rightside">Source</a>

#### type <a href="#associatedtype.ExecResult"
class="associatedtype">ExecResult</a>

</div>

<div id="associatedtype.NewState" class="section method">

<a href="../../src/vstd/logatom.rs.html#33"
class="src rightside">Source</a>

#### type <a href="#associatedtype.NewState" class="associatedtype">NewState</a>

</div>

</div>

## Dyn Compatibility<a href="#dyn-compatibility" class="anchor">§</a>

<div class="dyn-compatibility-info">

This trait is **not** [dyn
compatible](https://doc.rust-lang.org/1.92.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object
safety", so this trait is not object safe.*

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
