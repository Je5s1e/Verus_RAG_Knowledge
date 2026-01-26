<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)

</div>

# Module punctuated Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/punctuated.rs.html#1-1169"
class="src">Source</a> </span>

</div>

Expand description

<div class="docblock">

A punctuated sequence of syntax tree nodes separated by punctuation.

Lots of things in Rust are punctuated sequences.

- The fields of a struct are `Punctuated<Field, Token![,]>`.
- The segments of a path are `Punctuated<PathSegment, Token![::]>`.
- The bounds on a generic parameter are
  `Punctuated<TypeParamBound, Token![+]>`.
- The arguments to a function call are `Punctuated<Expr, Token![,]>`.

This module provides a common representation for these punctuated
sequences in the form of the
[`Punctuated<T, P>`](struct.Punctuated.html "struct verus_syn::punctuated::Punctuated")
type. We store a vector of pairs of syntax tree node + punctuation,
where every node in the sequence is followed by punctuation except for
possibly the final one.

<div class="example-wrap">

``` text
a_function_call(arg1, arg2, arg3);
                ~~~~^ ~~~~^ ~~~~
```

</div>

</div>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.IntoIter.html" class="struct"
title="struct verus_syn::punctuated::IntoIter">IntoIter</a>  
An iterator over owned values of type `T`.

<a href="struct.IntoPairs.html" class="struct"
title="struct verus_syn::punctuated::IntoPairs">IntoPairs</a>  
An iterator over owned pairs of type `Pair<T, P>`.

<a href="struct.Iter.html" class="struct"
title="struct verus_syn::punctuated::Iter">Iter</a>  
An iterator over borrowed values of type `&T`.

<a href="struct.IterMut.html" class="struct"
title="struct verus_syn::punctuated::IterMut">IterMut</a>  
An iterator over mutably borrowed values of type `&mut T`.

<a href="struct.Pairs.html" class="struct"
title="struct verus_syn::punctuated::Pairs">Pairs</a>  
An iterator over borrowed pairs of type `Pair<&T, &P>`.

<a href="struct.PairsMut.html" class="struct"
title="struct verus_syn::punctuated::PairsMut">PairsMut</a>  
An iterator over mutably borrowed pairs of type `Pair<&mut T, &mut P>`.

<a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>  
**A punctuated sequence of syntax tree nodes of type `T` separated by
punctuation of type `P`.**

## Enums<a href="#enums" class="anchor">§</a>

<a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>  
A single syntax tree node of type `T` followed by its trailing
punctuation of type `P` if any.

</div>

</div>
