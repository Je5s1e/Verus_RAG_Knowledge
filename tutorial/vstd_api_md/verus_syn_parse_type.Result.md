<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)::[parse](index.html)

</div>

# Type Alias <span class="type">Result</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/error.rs.html#15" class="src">Source</a>
</span>

</div>

``` rust
pub type Result<T> = Result<T, Error>;
```

Expand description

<div class="docblock">

The result of a Syn parser.

</div>

## Aliased Type<a href="#aliased-type" class="anchor">§</a>

``` rust
pub enum Result<T> {
    Ok(T),
    Err(Error),
}
```

## Variants<a href="#variants" class="anchor">§</a>

<div class="variants">

<div id="variant.Ok" class="section variant">

<a href="#variant.Ok" class="anchor">§</a><span class="since rightside"
title="Stable since Rust version 1.0.0">1.0.0</span>

### Ok(T)

</div>

<div class="docblock">

Contains the success value

</div>

<div id="variant.Err" class="section variant">

<a href="#variant.Err" class="anchor">§</a><span class="since rightside"
title="Stable since Rust version 1.0.0">1.0.0</span>

### Err(<a href="../struct.Error.html" class="struct"
title="struct verus_syn::Error">Error</a>)

</div>

<div class="docblock">

Contains the error value

</div>

</div>

</div>

</div>
