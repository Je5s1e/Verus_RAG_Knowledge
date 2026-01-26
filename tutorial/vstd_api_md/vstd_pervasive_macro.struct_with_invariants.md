<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[pervasive](index.html)

</div>

# Macro <span class="macro">struct_with_invariants</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_builtin_macros/lib.rs.html#313"
class="src">Source</a> </span>

</div>

``` rust
struct_with_invariants!() { /* proc-macro */ }
```

Expand description

<div class="docblock">

Macro to help set up boilerplate for specifying invariants when using
invariant-based datatypes.

This currently supports the `AtomicInvariant` and `LocalInvariant`
types, as well as all the `atomic_ghost` types (e.g., `AtomicU64`,
`AtomicBool`, and so on). It is important to first understand how these
types work. In particular, `LocalInvariant` (for example) takes three
type parameters, `K`, `V`, and `Pred: InvariantPredicate`. The
`InvariantPredicate` trait lets the user specify an invariant at the
static type level, while `K` allows the user to configure the invariant
upon construction. `AtomicInvariant` uses the same system, and the
`atomic_ghost` types are similar but use a different trait
(`AtomicInvariantPredicate`).

However, setting all this up in a typical application tends to involve a
bit of boilerplate. That’s where this macro comes in.

## <a href="#usage" class="doc-anchor">§</a>Usage

The `struct_with_invariants!` macro is used at the item level, and it
should contains a single struct declaration followed by a single
declaration of a `spec` function returning `bool`. However, this spec
function should not contain a boolean predicate as usual, but instead a
series of *invariant declarations*. Each invariant declaration applies
to a single field of the struct.

<div class="example-wrap">

``` rust
struct_with_invariants!{
    (pub)? struct $struct_name (<...>)? (where ...)? {
        ( (pub)? $field_name: $type, )*
    }

    (pub)? (open|closed)? spec fn(&self (, ...)?) $fn_name {
        ( InvariantDecl | BoolPredicateDecl )*
    }
}
```

</div>

A field of the struct, if it uses a supported type, may leave the type
*incomplete* by omitting some of its type parameters. The following are
valid incomplete types:

- `LocalInvariant<_, V, _>`
- `AtomicInvariant<_, V, _>`
- `AtomicBool<_, G, _>`
- `AtomicU64<_, G, _>`
  - … and so on for the other `atomic_ghost` types.

There must be exactly one invariant declaration for each incomplete type
used in the struct declaration. The macro uses invariant declarations to
fill in the type parameters.

The user can also provide boolean predicate declarations, which are
copied verbatim into the `$fn_name` definition. This is a convenience,
since it is common to want to add extra conditions, and it is fairly
straightforward. The complex part of the macro expansion in the
invariant declarations.

<div class="example-wrap">

``` rust
BoolPredicateDecl  :=  predicate { $bool_expr }

InvariantDecl  :=
    invariant on $field_name
        ( with ($dependencies) )?
        ( forall | ($ident: $type, )* | )?
        ( where ($where_expr) )?
        ( specifically ($specifically_expr) )?
        is ($params) {
            $bool_expr
        }
```

</div>

In the `InvariantDecl`, the user always needs to provide the following
data:

- The `$field_name` is the field that this invariant applies to (which
  must have an incomplete type as described above)
- The `$params` are the values constrained by the invariant.
  - For a `LocalInvariant<V>` or `AtomicInvariant<V>`, this should be a
    single parameter of type `V`.
  - For an `atomic_ghost` type, this should consist of two parameters,
    first the primitive type stored by the atomic, and secondly one of
    the ghost type, `G`. (For example, the type `AtomicBool<_, G, _>`
    should have two parameters here, `b: bool, g: G`.)
- Finally, the `$bool_expr` is the invariant predicate, which may
  reference any of the fields declared in `$dependencies`, or any of the
  params.

The other input clauses handle additional complexities that often comes
up. For example, it is often necessary for the invariant to refer to the
values of other fields in the struct.

- The `with` input gives the list of field names (other fields from the
  struct definition) that may be referenced from the body of this
  invariant. The graph of dependencies across all fields must be
  acyclic.

Finally, when the field is a *container* type, e.g.,
`vec: Vec<AtomicU64<_, G, _>>` or `opt: Option<AtomicU64<_, G, _>>`,
there are some additional complexities. We might need the invariant to
be conditional (e.g., for an optional, the invariant would only exist if
`opt is Some`). We might need to quantify over a variable (e.g., in a
vector, we want to specify an invariant for each element, element `i`
where `0 <= i < vec.len()`). Finally, we need to indicate the value
actually getting the invariant (e.g., `self.vec[i]`).

- The `forall` lets you specify additional bound variables. Everything
  after the `forall`—the `where`, the `specifically`, and finally the
  `$bool_expr$`—can all reference these bound variables.
- The `where` lets you specify an additional hypothesis that the
  invariant is dependent on.
- The `specifically` lets you indicate the value getting the invariant.

This all roughly means, “forall instantiations of the quantified
variables, if the condition `$where_expr` holds, then the value given by
`$specifically_expr` has the invariant given by `$bool_expr`. See the
detailed information on the macro-expansion below for more details.

Given all the information from the `InvariantDecl`, the macro fills in
the `_` placeholders as follows:

- The macro fills in the `K` type as the types of the fields marked as
  dependencies and the quantified variables in the forall (packing all
  these types into a tuple if necessary).
- The macro fills in the `Pred` type by creating a new type and
  implementing the appropriate trait with the user-provided predicate.

## <a href="#example-todo" class="doc-anchor">§</a>Example (TODO)

## <a href="#example-using-a-container-type-todo" class="doc-anchor">§</a>Example using a container type (TODO)

## <a href="#macro-expansion-todo" class="doc-anchor">§</a>Macro Expansion (TODO)

</div>

</div>

</div>
