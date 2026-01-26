<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](../index.html)

</div>

# Module visit Copy item path

<span class="sub-heading"><a href="../../src/syn/gen/visit.rs.html#4-3941" class="src">Source</a>
</span>

</div>

Expand description

<div class="docblock">

Syntax tree traversal to walk a shared borrow of a syntax tree.

Each method of the [`Visit`](trait.Visit.html "trait syn::visit::Visit")
trait is a hook that can be overridden to customize the behavior when
visiting the corresponding type of node. By default, every method
recursively visits the substructure of the input by invoking the right
visitor method of each of its fields.

<div class="example-wrap">

``` rust
pub trait Visit<'ast> {
    /* ... */

    fn visit_expr_binary(&mut self, node: &'ast ExprBinary) {
        visit_expr_binary(self, node);
    }

    /* ... */
}

pub fn visit_expr_binary<'ast, V>(v: &mut V, node: &'ast ExprBinary)
where
    V: Visit<'ast> + ?Sized,
{
    for attr in &node.attrs {
        v.visit_attribute(attr);
    }
    v.visit_expr(&*node.left);
    v.visit_bin_op(&node.op);
    v.visit_expr(&*node.right);
}

/* ... */
```

</div>

  

## <a href="#example" class="doc-anchor">§</a>Example

This visitor will print the name of every freestanding function in the
syntax tree, including nested functions.

<div class="example-wrap">

``` rust
// [dependencies]
// quote = "1.0"
// syn = { version = "2.0", features = ["full", "visit"] }

use quote::quote;
use syn::visit::{self, Visit};
use syn::{File, ItemFn};

struct FnVisitor;

impl<'ast> Visit<'ast> for FnVisitor {
    fn visit_item_fn(&mut self, node: &'ast ItemFn) {
        println!("Function with name={}", node.sig.ident);

        // Delegate to the default impl to visit any nested functions.
        visit::visit_item_fn(self, node);
    }
}

fn main() {
    let code = quote! {
        pub fn f() {
            fn g() {}
        }
    };

    let syntax_tree: File = syn::parse2(code).unwrap();
    FnVisitor.visit_file(&syntax_tree);
}
```

</div>

The `'ast` lifetime on the input references means that the syntax tree
outlives the complete recursive visit call, so the visitor is allowed to
hold on to references into the syntax tree.

<div class="example-wrap">

``` rust
use quote::quote;
use syn::visit::{self, Visit};
use syn::{File, ItemFn};

struct FnVisitor<'ast> {
    functions: Vec<&'ast ItemFn>,
}

impl<'ast> Visit<'ast> for FnVisitor<'ast> {
    fn visit_item_fn(&mut self, node: &'ast ItemFn) {
        self.functions.push(node);
        visit::visit_item_fn(self, node);
    }
}

fn main() {
    let code = quote! {
        pub fn f() {
            fn g() {}
        }
    };

    let syntax_tree: File = syn::parse2(code).unwrap();
    let mut visitor = FnVisitor { functions: Vec::new() };
    visitor.visit_file(&syntax_tree);
    for f in visitor.functions {
        println!("Function with name={}", f.sig.ident);
    }
}
```

</div>

</div>

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.Visit.html" class="trait"
title="trait syn::visit::Visit">Visit</a>  
Syntax tree traversal to walk a shared borrow of a syntax tree.

## Functions<a href="#functions" class="anchor">§</a>

<a href="fn.visit_abi.html" class="fn"
title="fn syn::visit::visit_abi">visit_abi</a>

<a href="fn.visit_angle_bracketed_generic_arguments.html" class="fn"
title="fn syn::visit::visit_angle_bracketed_generic_arguments">visit_angle_bracketed_generic_arguments</a>

<a href="fn.visit_arm.html" class="fn"
title="fn syn::visit::visit_arm">visit_arm</a>

<a href="fn.visit_assoc_const.html" class="fn"
title="fn syn::visit::visit_assoc_const">visit_assoc_const</a>

<a href="fn.visit_assoc_type.html" class="fn"
title="fn syn::visit::visit_assoc_type">visit_assoc_type</a>

<a href="fn.visit_attr_style.html" class="fn"
title="fn syn::visit::visit_attr_style">visit_attr_style</a>

<a href="fn.visit_attribute.html" class="fn"
title="fn syn::visit::visit_attribute">visit_attribute</a>

<a href="fn.visit_bare_fn_arg.html" class="fn"
title="fn syn::visit::visit_bare_fn_arg">visit_bare_fn_arg</a>

<a href="fn.visit_bare_variadic.html" class="fn"
title="fn syn::visit::visit_bare_variadic">visit_bare_variadic</a>

<a href="fn.visit_bin_op.html" class="fn"
title="fn syn::visit::visit_bin_op">visit_bin_op</a>

<a href="fn.visit_block.html" class="fn"
title="fn syn::visit::visit_block">visit_block</a>

<a href="fn.visit_bound_lifetimes.html" class="fn"
title="fn syn::visit::visit_bound_lifetimes">visit_bound_lifetimes</a>

<a href="fn.visit_captured_param.html" class="fn"
title="fn syn::visit::visit_captured_param">visit_captured_param</a>

<a href="fn.visit_const_param.html" class="fn"
title="fn syn::visit::visit_const_param">visit_const_param</a>

<a href="fn.visit_constraint.html" class="fn"
title="fn syn::visit::visit_constraint">visit_constraint</a>

<a href="fn.visit_data.html" class="fn"
title="fn syn::visit::visit_data">visit_data</a>

<a href="fn.visit_data_enum.html" class="fn"
title="fn syn::visit::visit_data_enum">visit_data_enum</a>

<a href="fn.visit_data_struct.html" class="fn"
title="fn syn::visit::visit_data_struct">visit_data_struct</a>

<a href="fn.visit_data_union.html" class="fn"
title="fn syn::visit::visit_data_union">visit_data_union</a>

<a href="fn.visit_derive_input.html" class="fn"
title="fn syn::visit::visit_derive_input">visit_derive_input</a>

<a href="fn.visit_expr.html" class="fn"
title="fn syn::visit::visit_expr">visit_expr</a>

<a href="fn.visit_expr_array.html" class="fn"
title="fn syn::visit::visit_expr_array">visit_expr_array</a>

<a href="fn.visit_expr_assign.html" class="fn"
title="fn syn::visit::visit_expr_assign">visit_expr_assign</a>

<a href="fn.visit_expr_async.html" class="fn"
title="fn syn::visit::visit_expr_async">visit_expr_async</a>

<a href="fn.visit_expr_await.html" class="fn"
title="fn syn::visit::visit_expr_await">visit_expr_await</a>

<a href="fn.visit_expr_binary.html" class="fn"
title="fn syn::visit::visit_expr_binary">visit_expr_binary</a>

<a href="fn.visit_expr_block.html" class="fn"
title="fn syn::visit::visit_expr_block">visit_expr_block</a>

<a href="fn.visit_expr_break.html" class="fn"
title="fn syn::visit::visit_expr_break">visit_expr_break</a>

<a href="fn.visit_expr_call.html" class="fn"
title="fn syn::visit::visit_expr_call">visit_expr_call</a>

<a href="fn.visit_expr_cast.html" class="fn"
title="fn syn::visit::visit_expr_cast">visit_expr_cast</a>

<a href="fn.visit_expr_closure.html" class="fn"
title="fn syn::visit::visit_expr_closure">visit_expr_closure</a>

<a href="fn.visit_expr_const.html" class="fn"
title="fn syn::visit::visit_expr_const">visit_expr_const</a>

<a href="fn.visit_expr_continue.html" class="fn"
title="fn syn::visit::visit_expr_continue">visit_expr_continue</a>

<a href="fn.visit_expr_field.html" class="fn"
title="fn syn::visit::visit_expr_field">visit_expr_field</a>

<a href="fn.visit_expr_for_loop.html" class="fn"
title="fn syn::visit::visit_expr_for_loop">visit_expr_for_loop</a>

<a href="fn.visit_expr_group.html" class="fn"
title="fn syn::visit::visit_expr_group">visit_expr_group</a>

<a href="fn.visit_expr_if.html" class="fn"
title="fn syn::visit::visit_expr_if">visit_expr_if</a>

<a href="fn.visit_expr_index.html" class="fn"
title="fn syn::visit::visit_expr_index">visit_expr_index</a>

<a href="fn.visit_expr_infer.html" class="fn"
title="fn syn::visit::visit_expr_infer">visit_expr_infer</a>

<a href="fn.visit_expr_let.html" class="fn"
title="fn syn::visit::visit_expr_let">visit_expr_let</a>

<a href="fn.visit_expr_lit.html" class="fn"
title="fn syn::visit::visit_expr_lit">visit_expr_lit</a>

<a href="fn.visit_expr_loop.html" class="fn"
title="fn syn::visit::visit_expr_loop">visit_expr_loop</a>

<a href="fn.visit_expr_macro.html" class="fn"
title="fn syn::visit::visit_expr_macro">visit_expr_macro</a>

<a href="fn.visit_expr_match.html" class="fn"
title="fn syn::visit::visit_expr_match">visit_expr_match</a>

<a href="fn.visit_expr_method_call.html" class="fn"
title="fn syn::visit::visit_expr_method_call">visit_expr_method_call</a>

<a href="fn.visit_expr_paren.html" class="fn"
title="fn syn::visit::visit_expr_paren">visit_expr_paren</a>

<a href="fn.visit_expr_path.html" class="fn"
title="fn syn::visit::visit_expr_path">visit_expr_path</a>

<a href="fn.visit_expr_range.html" class="fn"
title="fn syn::visit::visit_expr_range">visit_expr_range</a>

<a href="fn.visit_expr_raw_addr.html" class="fn"
title="fn syn::visit::visit_expr_raw_addr">visit_expr_raw_addr</a>

<a href="fn.visit_expr_reference.html" class="fn"
title="fn syn::visit::visit_expr_reference">visit_expr_reference</a>

<a href="fn.visit_expr_repeat.html" class="fn"
title="fn syn::visit::visit_expr_repeat">visit_expr_repeat</a>

<a href="fn.visit_expr_return.html" class="fn"
title="fn syn::visit::visit_expr_return">visit_expr_return</a>

<a href="fn.visit_expr_struct.html" class="fn"
title="fn syn::visit::visit_expr_struct">visit_expr_struct</a>

<a href="fn.visit_expr_try.html" class="fn"
title="fn syn::visit::visit_expr_try">visit_expr_try</a>

<a href="fn.visit_expr_try_block.html" class="fn"
title="fn syn::visit::visit_expr_try_block">visit_expr_try_block</a>

<a href="fn.visit_expr_tuple.html" class="fn"
title="fn syn::visit::visit_expr_tuple">visit_expr_tuple</a>

<a href="fn.visit_expr_unary.html" class="fn"
title="fn syn::visit::visit_expr_unary">visit_expr_unary</a>

<a href="fn.visit_expr_unsafe.html" class="fn"
title="fn syn::visit::visit_expr_unsafe">visit_expr_unsafe</a>

<a href="fn.visit_expr_while.html" class="fn"
title="fn syn::visit::visit_expr_while">visit_expr_while</a>

<a href="fn.visit_expr_yield.html" class="fn"
title="fn syn::visit::visit_expr_yield">visit_expr_yield</a>

<a href="fn.visit_field.html" class="fn"
title="fn syn::visit::visit_field">visit_field</a>

<a href="fn.visit_field_mutability.html" class="fn"
title="fn syn::visit::visit_field_mutability">visit_field_mutability</a>

<a href="fn.visit_field_pat.html" class="fn"
title="fn syn::visit::visit_field_pat">visit_field_pat</a>

<a href="fn.visit_field_value.html" class="fn"
title="fn syn::visit::visit_field_value">visit_field_value</a>

<a href="fn.visit_fields.html" class="fn"
title="fn syn::visit::visit_fields">visit_fields</a>

<a href="fn.visit_fields_named.html" class="fn"
title="fn syn::visit::visit_fields_named">visit_fields_named</a>

<a href="fn.visit_fields_unnamed.html" class="fn"
title="fn syn::visit::visit_fields_unnamed">visit_fields_unnamed</a>

<a href="fn.visit_file.html" class="fn"
title="fn syn::visit::visit_file">visit_file</a>

<a href="fn.visit_fn_arg.html" class="fn"
title="fn syn::visit::visit_fn_arg">visit_fn_arg</a>

<a href="fn.visit_foreign_item.html" class="fn"
title="fn syn::visit::visit_foreign_item">visit_foreign_item</a>

<a href="fn.visit_foreign_item_fn.html" class="fn"
title="fn syn::visit::visit_foreign_item_fn">visit_foreign_item_fn</a>

<a href="fn.visit_foreign_item_macro.html" class="fn"
title="fn syn::visit::visit_foreign_item_macro">visit_foreign_item_macro</a>

<a href="fn.visit_foreign_item_static.html" class="fn"
title="fn syn::visit::visit_foreign_item_static">visit_foreign_item_static</a>

<a href="fn.visit_foreign_item_type.html" class="fn"
title="fn syn::visit::visit_foreign_item_type">visit_foreign_item_type</a>

<a href="fn.visit_generic_argument.html" class="fn"
title="fn syn::visit::visit_generic_argument">visit_generic_argument</a>

<a href="fn.visit_generic_param.html" class="fn"
title="fn syn::visit::visit_generic_param">visit_generic_param</a>

<a href="fn.visit_generics.html" class="fn"
title="fn syn::visit::visit_generics">visit_generics</a>

<a href="fn.visit_ident.html" class="fn"
title="fn syn::visit::visit_ident">visit_ident</a>

<a href="fn.visit_impl_item.html" class="fn"
title="fn syn::visit::visit_impl_item">visit_impl_item</a>

<a href="fn.visit_impl_item_const.html" class="fn"
title="fn syn::visit::visit_impl_item_const">visit_impl_item_const</a>

<a href="fn.visit_impl_item_fn.html" class="fn"
title="fn syn::visit::visit_impl_item_fn">visit_impl_item_fn</a>

<a href="fn.visit_impl_item_macro.html" class="fn"
title="fn syn::visit::visit_impl_item_macro">visit_impl_item_macro</a>

<a href="fn.visit_impl_item_type.html" class="fn"
title="fn syn::visit::visit_impl_item_type">visit_impl_item_type</a>

<a href="fn.visit_impl_restriction.html" class="fn"
title="fn syn::visit::visit_impl_restriction">visit_impl_restriction</a>

<a href="fn.visit_index.html" class="fn"
title="fn syn::visit::visit_index">visit_index</a>

<a href="fn.visit_item.html" class="fn"
title="fn syn::visit::visit_item">visit_item</a>

<a href="fn.visit_item_const.html" class="fn"
title="fn syn::visit::visit_item_const">visit_item_const</a>

<a href="fn.visit_item_enum.html" class="fn"
title="fn syn::visit::visit_item_enum">visit_item_enum</a>

<a href="fn.visit_item_extern_crate.html" class="fn"
title="fn syn::visit::visit_item_extern_crate">visit_item_extern_crate</a>

<a href="fn.visit_item_fn.html" class="fn"
title="fn syn::visit::visit_item_fn">visit_item_fn</a>

<a href="fn.visit_item_foreign_mod.html" class="fn"
title="fn syn::visit::visit_item_foreign_mod">visit_item_foreign_mod</a>

<a href="fn.visit_item_impl.html" class="fn"
title="fn syn::visit::visit_item_impl">visit_item_impl</a>

<a href="fn.visit_item_macro.html" class="fn"
title="fn syn::visit::visit_item_macro">visit_item_macro</a>

<a href="fn.visit_item_mod.html" class="fn"
title="fn syn::visit::visit_item_mod">visit_item_mod</a>

<a href="fn.visit_item_static.html" class="fn"
title="fn syn::visit::visit_item_static">visit_item_static</a>

<a href="fn.visit_item_struct.html" class="fn"
title="fn syn::visit::visit_item_struct">visit_item_struct</a>

<a href="fn.visit_item_trait.html" class="fn"
title="fn syn::visit::visit_item_trait">visit_item_trait</a>

<a href="fn.visit_item_trait_alias.html" class="fn"
title="fn syn::visit::visit_item_trait_alias">visit_item_trait_alias</a>

<a href="fn.visit_item_type.html" class="fn"
title="fn syn::visit::visit_item_type">visit_item_type</a>

<a href="fn.visit_item_union.html" class="fn"
title="fn syn::visit::visit_item_union">visit_item_union</a>

<a href="fn.visit_item_use.html" class="fn"
title="fn syn::visit::visit_item_use">visit_item_use</a>

<a href="fn.visit_label.html" class="fn"
title="fn syn::visit::visit_label">visit_label</a>

<a href="fn.visit_lifetime.html" class="fn"
title="fn syn::visit::visit_lifetime">visit_lifetime</a>

<a href="fn.visit_lifetime_param.html" class="fn"
title="fn syn::visit::visit_lifetime_param">visit_lifetime_param</a>

<a href="fn.visit_lit.html" class="fn"
title="fn syn::visit::visit_lit">visit_lit</a>

<a href="fn.visit_lit_bool.html" class="fn"
title="fn syn::visit::visit_lit_bool">visit_lit_bool</a>

<a href="fn.visit_lit_byte.html" class="fn"
title="fn syn::visit::visit_lit_byte">visit_lit_byte</a>

<a href="fn.visit_lit_byte_str.html" class="fn"
title="fn syn::visit::visit_lit_byte_str">visit_lit_byte_str</a>

<a href="fn.visit_lit_char.html" class="fn"
title="fn syn::visit::visit_lit_char">visit_lit_char</a>

<a href="fn.visit_lit_cstr.html" class="fn"
title="fn syn::visit::visit_lit_cstr">visit_lit_cstr</a>

<a href="fn.visit_lit_float.html" class="fn"
title="fn syn::visit::visit_lit_float">visit_lit_float</a>

<a href="fn.visit_lit_int.html" class="fn"
title="fn syn::visit::visit_lit_int">visit_lit_int</a>

<a href="fn.visit_lit_str.html" class="fn"
title="fn syn::visit::visit_lit_str">visit_lit_str</a>

<a href="fn.visit_local.html" class="fn"
title="fn syn::visit::visit_local">visit_local</a>

<a href="fn.visit_local_init.html" class="fn"
title="fn syn::visit::visit_local_init">visit_local_init</a>

<a href="fn.visit_macro.html" class="fn"
title="fn syn::visit::visit_macro">visit_macro</a>

<a href="fn.visit_macro_delimiter.html" class="fn"
title="fn syn::visit::visit_macro_delimiter">visit_macro_delimiter</a>

<a href="fn.visit_member.html" class="fn"
title="fn syn::visit::visit_member">visit_member</a>

<a href="fn.visit_meta.html" class="fn"
title="fn syn::visit::visit_meta">visit_meta</a>

<a href="fn.visit_meta_list.html" class="fn"
title="fn syn::visit::visit_meta_list">visit_meta_list</a>

<a href="fn.visit_meta_name_value.html" class="fn"
title="fn syn::visit::visit_meta_name_value">visit_meta_name_value</a>

<a href="fn.visit_parenthesized_generic_arguments.html" class="fn"
title="fn syn::visit::visit_parenthesized_generic_arguments">visit_parenthesized_generic_arguments</a>

<a href="fn.visit_pat.html" class="fn"
title="fn syn::visit::visit_pat">visit_pat</a>

<a href="fn.visit_pat_ident.html" class="fn"
title="fn syn::visit::visit_pat_ident">visit_pat_ident</a>

<a href="fn.visit_pat_or.html" class="fn"
title="fn syn::visit::visit_pat_or">visit_pat_or</a>

<a href="fn.visit_pat_paren.html" class="fn"
title="fn syn::visit::visit_pat_paren">visit_pat_paren</a>

<a href="fn.visit_pat_reference.html" class="fn"
title="fn syn::visit::visit_pat_reference">visit_pat_reference</a>

<a href="fn.visit_pat_rest.html" class="fn"
title="fn syn::visit::visit_pat_rest">visit_pat_rest</a>

<a href="fn.visit_pat_slice.html" class="fn"
title="fn syn::visit::visit_pat_slice">visit_pat_slice</a>

<a href="fn.visit_pat_struct.html" class="fn"
title="fn syn::visit::visit_pat_struct">visit_pat_struct</a>

<a href="fn.visit_pat_tuple.html" class="fn"
title="fn syn::visit::visit_pat_tuple">visit_pat_tuple</a>

<a href="fn.visit_pat_tuple_struct.html" class="fn"
title="fn syn::visit::visit_pat_tuple_struct">visit_pat_tuple_struct</a>

<a href="fn.visit_pat_type.html" class="fn"
title="fn syn::visit::visit_pat_type">visit_pat_type</a>

<a href="fn.visit_pat_wild.html" class="fn"
title="fn syn::visit::visit_pat_wild">visit_pat_wild</a>

<a href="fn.visit_path.html" class="fn"
title="fn syn::visit::visit_path">visit_path</a>

<a href="fn.visit_path_arguments.html" class="fn"
title="fn syn::visit::visit_path_arguments">visit_path_arguments</a>

<a href="fn.visit_path_segment.html" class="fn"
title="fn syn::visit::visit_path_segment">visit_path_segment</a>

<a href="fn.visit_pointer_mutability.html" class="fn"
title="fn syn::visit::visit_pointer_mutability">visit_pointer_mutability</a>

<a href="fn.visit_precise_capture.html" class="fn"
title="fn syn::visit::visit_precise_capture">visit_precise_capture</a>

<a href="fn.visit_predicate_lifetime.html" class="fn"
title="fn syn::visit::visit_predicate_lifetime">visit_predicate_lifetime</a>

<a href="fn.visit_predicate_type.html" class="fn"
title="fn syn::visit::visit_predicate_type">visit_predicate_type</a>

<a href="fn.visit_qself.html" class="fn"
title="fn syn::visit::visit_qself">visit_qself</a>

<a href="fn.visit_range_limits.html" class="fn"
title="fn syn::visit::visit_range_limits">visit_range_limits</a>

<a href="fn.visit_receiver.html" class="fn"
title="fn syn::visit::visit_receiver">visit_receiver</a>

<a href="fn.visit_return_type.html" class="fn"
title="fn syn::visit::visit_return_type">visit_return_type</a>

<a href="fn.visit_signature.html" class="fn"
title="fn syn::visit::visit_signature">visit_signature</a>

<a href="fn.visit_span.html" class="fn"
title="fn syn::visit::visit_span">visit_span</a>

<a href="fn.visit_static_mutability.html" class="fn"
title="fn syn::visit::visit_static_mutability">visit_static_mutability</a>

<a href="fn.visit_stmt.html" class="fn"
title="fn syn::visit::visit_stmt">visit_stmt</a>

<a href="fn.visit_stmt_macro.html" class="fn"
title="fn syn::visit::visit_stmt_macro">visit_stmt_macro</a>

<a href="fn.visit_trait_bound.html" class="fn"
title="fn syn::visit::visit_trait_bound">visit_trait_bound</a>

<a href="fn.visit_trait_bound_modifier.html" class="fn"
title="fn syn::visit::visit_trait_bound_modifier">visit_trait_bound_modifier</a>

<a href="fn.visit_trait_item.html" class="fn"
title="fn syn::visit::visit_trait_item">visit_trait_item</a>

<a href="fn.visit_trait_item_const.html" class="fn"
title="fn syn::visit::visit_trait_item_const">visit_trait_item_const</a>

<a href="fn.visit_trait_item_fn.html" class="fn"
title="fn syn::visit::visit_trait_item_fn">visit_trait_item_fn</a>

<a href="fn.visit_trait_item_macro.html" class="fn"
title="fn syn::visit::visit_trait_item_macro">visit_trait_item_macro</a>

<a href="fn.visit_trait_item_type.html" class="fn"
title="fn syn::visit::visit_trait_item_type">visit_trait_item_type</a>

<a href="fn.visit_type.html" class="fn"
title="fn syn::visit::visit_type">visit_type</a>

<a href="fn.visit_type_array.html" class="fn"
title="fn syn::visit::visit_type_array">visit_type_array</a>

<a href="fn.visit_type_bare_fn.html" class="fn"
title="fn syn::visit::visit_type_bare_fn">visit_type_bare_fn</a>

<a href="fn.visit_type_group.html" class="fn"
title="fn syn::visit::visit_type_group">visit_type_group</a>

<a href="fn.visit_type_impl_trait.html" class="fn"
title="fn syn::visit::visit_type_impl_trait">visit_type_impl_trait</a>

<a href="fn.visit_type_infer.html" class="fn"
title="fn syn::visit::visit_type_infer">visit_type_infer</a>

<a href="fn.visit_type_macro.html" class="fn"
title="fn syn::visit::visit_type_macro">visit_type_macro</a>

<a href="fn.visit_type_never.html" class="fn"
title="fn syn::visit::visit_type_never">visit_type_never</a>

<a href="fn.visit_type_param.html" class="fn"
title="fn syn::visit::visit_type_param">visit_type_param</a>

<a href="fn.visit_type_param_bound.html" class="fn"
title="fn syn::visit::visit_type_param_bound">visit_type_param_bound</a>

<a href="fn.visit_type_paren.html" class="fn"
title="fn syn::visit::visit_type_paren">visit_type_paren</a>

<a href="fn.visit_type_path.html" class="fn"
title="fn syn::visit::visit_type_path">visit_type_path</a>

<a href="fn.visit_type_ptr.html" class="fn"
title="fn syn::visit::visit_type_ptr">visit_type_ptr</a>

<a href="fn.visit_type_reference.html" class="fn"
title="fn syn::visit::visit_type_reference">visit_type_reference</a>

<a href="fn.visit_type_slice.html" class="fn"
title="fn syn::visit::visit_type_slice">visit_type_slice</a>

<a href="fn.visit_type_trait_object.html" class="fn"
title="fn syn::visit::visit_type_trait_object">visit_type_trait_object</a>

<a href="fn.visit_type_tuple.html" class="fn"
title="fn syn::visit::visit_type_tuple">visit_type_tuple</a>

<a href="fn.visit_un_op.html" class="fn"
title="fn syn::visit::visit_un_op">visit_un_op</a>

<a href="fn.visit_use_glob.html" class="fn"
title="fn syn::visit::visit_use_glob">visit_use_glob</a>

<a href="fn.visit_use_group.html" class="fn"
title="fn syn::visit::visit_use_group">visit_use_group</a>

<a href="fn.visit_use_name.html" class="fn"
title="fn syn::visit::visit_use_name">visit_use_name</a>

<a href="fn.visit_use_path.html" class="fn"
title="fn syn::visit::visit_use_path">visit_use_path</a>

<a href="fn.visit_use_rename.html" class="fn"
title="fn syn::visit::visit_use_rename">visit_use_rename</a>

<a href="fn.visit_use_tree.html" class="fn"
title="fn syn::visit::visit_use_tree">visit_use_tree</a>

<a href="fn.visit_variadic.html" class="fn"
title="fn syn::visit::visit_variadic">visit_variadic</a>

<a href="fn.visit_variant.html" class="fn"
title="fn syn::visit::visit_variant">visit_variant</a>

<a href="fn.visit_vis_restricted.html" class="fn"
title="fn syn::visit::visit_vis_restricted">visit_vis_restricted</a>

<a href="fn.visit_visibility.html" class="fn"
title="fn syn::visit::visit_visibility">visit_visibility</a>

<a href="fn.visit_where_clause.html" class="fn"
title="fn syn::visit::visit_where_clause">visit_where_clause</a>

<a href="fn.visit_where_predicate.html" class="fn"
title="fn syn::visit::visit_where_predicate">visit_where_predicate</a>

</div>

</div>
