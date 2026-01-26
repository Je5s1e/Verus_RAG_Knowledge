<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](../index.html)::[visit_mut](index.html)

</div>

# Trait <span class="trait">VisitMut</span> Copy item path

<span class="sub-heading"><a href="../../src/syn/gen/visit_mut.rs.html#31-955"
class="src">Source</a> </span>

</div>

``` rust
pub trait VisitMut {
Show 189 methods    // Provided methods
    fn visit_abi_mut(&mut self, i: &mut Abi) { ... }
    fn visit_angle_bracketed_generic_arguments_mut(
        &mut self,
        i: &mut AngleBracketedGenericArguments,
    ) { ... }
    fn visit_arm_mut(&mut self, i: &mut Arm) { ... }
    fn visit_assoc_const_mut(&mut self, i: &mut AssocConst) { ... }
    fn visit_assoc_type_mut(&mut self, i: &mut AssocType) { ... }
    fn visit_attr_style_mut(&mut self, i: &mut AttrStyle) { ... }
    fn visit_attribute_mut(&mut self, i: &mut Attribute) { ... }
    fn visit_attributes_mut(&mut self, i: &mut Vec<Attribute>) { ... }
    fn visit_bare_fn_arg_mut(&mut self, i: &mut BareFnArg) { ... }
    fn visit_bare_variadic_mut(&mut self, i: &mut BareVariadic) { ... }
    fn visit_bin_op_mut(&mut self, i: &mut BinOp) { ... }
    fn visit_block_mut(&mut self, i: &mut Block) { ... }
    fn visit_bound_lifetimes_mut(&mut self, i: &mut BoundLifetimes) { ... }
    fn visit_captured_param_mut(&mut self, i: &mut CapturedParam) { ... }
    fn visit_const_param_mut(&mut self, i: &mut ConstParam) { ... }
    fn visit_constraint_mut(&mut self, i: &mut Constraint) { ... }
    fn visit_data_mut(&mut self, i: &mut Data) { ... }
    fn visit_data_enum_mut(&mut self, i: &mut DataEnum) { ... }
    fn visit_data_struct_mut(&mut self, i: &mut DataStruct) { ... }
    fn visit_data_union_mut(&mut self, i: &mut DataUnion) { ... }
    fn visit_derive_input_mut(&mut self, i: &mut DeriveInput) { ... }
    fn visit_expr_mut(&mut self, i: &mut Expr) { ... }
    fn visit_expr_array_mut(&mut self, i: &mut ExprArray) { ... }
    fn visit_expr_assign_mut(&mut self, i: &mut ExprAssign) { ... }
    fn visit_expr_async_mut(&mut self, i: &mut ExprAsync) { ... }
    fn visit_expr_await_mut(&mut self, i: &mut ExprAwait) { ... }
    fn visit_expr_binary_mut(&mut self, i: &mut ExprBinary) { ... }
    fn visit_expr_block_mut(&mut self, i: &mut ExprBlock) { ... }
    fn visit_expr_break_mut(&mut self, i: &mut ExprBreak) { ... }
    fn visit_expr_call_mut(&mut self, i: &mut ExprCall) { ... }
    fn visit_expr_cast_mut(&mut self, i: &mut ExprCast) { ... }
    fn visit_expr_closure_mut(&mut self, i: &mut ExprClosure) { ... }
    fn visit_expr_const_mut(&mut self, i: &mut ExprConst) { ... }
    fn visit_expr_continue_mut(&mut self, i: &mut ExprContinue) { ... }
    fn visit_expr_field_mut(&mut self, i: &mut ExprField) { ... }
    fn visit_expr_for_loop_mut(&mut self, i: &mut ExprForLoop) { ... }
    fn visit_expr_group_mut(&mut self, i: &mut ExprGroup) { ... }
    fn visit_expr_if_mut(&mut self, i: &mut ExprIf) { ... }
    fn visit_expr_index_mut(&mut self, i: &mut ExprIndex) { ... }
    fn visit_expr_infer_mut(&mut self, i: &mut ExprInfer) { ... }
    fn visit_expr_let_mut(&mut self, i: &mut ExprLet) { ... }
    fn visit_expr_lit_mut(&mut self, i: &mut ExprLit) { ... }
    fn visit_expr_loop_mut(&mut self, i: &mut ExprLoop) { ... }
    fn visit_expr_macro_mut(&mut self, i: &mut ExprMacro) { ... }
    fn visit_expr_match_mut(&mut self, i: &mut ExprMatch) { ... }
    fn visit_expr_method_call_mut(&mut self, i: &mut ExprMethodCall) { ... }
    fn visit_expr_paren_mut(&mut self, i: &mut ExprParen) { ... }
    fn visit_expr_path_mut(&mut self, i: &mut ExprPath) { ... }
    fn visit_expr_range_mut(&mut self, i: &mut ExprRange) { ... }
    fn visit_expr_raw_addr_mut(&mut self, i: &mut ExprRawAddr) { ... }
    fn visit_expr_reference_mut(&mut self, i: &mut ExprReference) { ... }
    fn visit_expr_repeat_mut(&mut self, i: &mut ExprRepeat) { ... }
    fn visit_expr_return_mut(&mut self, i: &mut ExprReturn) { ... }
    fn visit_expr_struct_mut(&mut self, i: &mut ExprStruct) { ... }
    fn visit_expr_try_mut(&mut self, i: &mut ExprTry) { ... }
    fn visit_expr_try_block_mut(&mut self, i: &mut ExprTryBlock) { ... }
    fn visit_expr_tuple_mut(&mut self, i: &mut ExprTuple) { ... }
    fn visit_expr_unary_mut(&mut self, i: &mut ExprUnary) { ... }
    fn visit_expr_unsafe_mut(&mut self, i: &mut ExprUnsafe) { ... }
    fn visit_expr_while_mut(&mut self, i: &mut ExprWhile) { ... }
    fn visit_expr_yield_mut(&mut self, i: &mut ExprYield) { ... }
    fn visit_field_mut(&mut self, i: &mut Field) { ... }
    fn visit_field_mutability_mut(&mut self, i: &mut FieldMutability) { ... }
    fn visit_field_pat_mut(&mut self, i: &mut FieldPat) { ... }
    fn visit_field_value_mut(&mut self, i: &mut FieldValue) { ... }
    fn visit_fields_mut(&mut self, i: &mut Fields) { ... }
    fn visit_fields_named_mut(&mut self, i: &mut FieldsNamed) { ... }
    fn visit_fields_unnamed_mut(&mut self, i: &mut FieldsUnnamed) { ... }
    fn visit_file_mut(&mut self, i: &mut File) { ... }
    fn visit_fn_arg_mut(&mut self, i: &mut FnArg) { ... }
    fn visit_foreign_item_mut(&mut self, i: &mut ForeignItem) { ... }
    fn visit_foreign_item_fn_mut(&mut self, i: &mut ForeignItemFn) { ... }
    fn visit_foreign_item_macro_mut(&mut self, i: &mut ForeignItemMacro) { ... }
    fn visit_foreign_item_static_mut(&mut self, i: &mut ForeignItemStatic) { ... }
    fn visit_foreign_item_type_mut(&mut self, i: &mut ForeignItemType) { ... }
    fn visit_generic_argument_mut(&mut self, i: &mut GenericArgument) { ... }
    fn visit_generic_param_mut(&mut self, i: &mut GenericParam) { ... }
    fn visit_generics_mut(&mut self, i: &mut Generics) { ... }
    fn visit_ident_mut(&mut self, i: &mut Ident) { ... }
    fn visit_impl_item_mut(&mut self, i: &mut ImplItem) { ... }
    fn visit_impl_item_const_mut(&mut self, i: &mut ImplItemConst) { ... }
    fn visit_impl_item_fn_mut(&mut self, i: &mut ImplItemFn) { ... }
    fn visit_impl_item_macro_mut(&mut self, i: &mut ImplItemMacro) { ... }
    fn visit_impl_item_type_mut(&mut self, i: &mut ImplItemType) { ... }
    fn visit_impl_restriction_mut(&mut self, i: &mut ImplRestriction) { ... }
    fn visit_index_mut(&mut self, i: &mut Index) { ... }
    fn visit_item_mut(&mut self, i: &mut Item) { ... }
    fn visit_item_const_mut(&mut self, i: &mut ItemConst) { ... }
    fn visit_item_enum_mut(&mut self, i: &mut ItemEnum) { ... }
    fn visit_item_extern_crate_mut(&mut self, i: &mut ItemExternCrate) { ... }
    fn visit_item_fn_mut(&mut self, i: &mut ItemFn) { ... }
    fn visit_item_foreign_mod_mut(&mut self, i: &mut ItemForeignMod) { ... }
    fn visit_item_impl_mut(&mut self, i: &mut ItemImpl) { ... }
    fn visit_item_macro_mut(&mut self, i: &mut ItemMacro) { ... }
    fn visit_item_mod_mut(&mut self, i: &mut ItemMod) { ... }
    fn visit_item_static_mut(&mut self, i: &mut ItemStatic) { ... }
    fn visit_item_struct_mut(&mut self, i: &mut ItemStruct) { ... }
    fn visit_item_trait_mut(&mut self, i: &mut ItemTrait) { ... }
    fn visit_item_trait_alias_mut(&mut self, i: &mut ItemTraitAlias) { ... }
    fn visit_item_type_mut(&mut self, i: &mut ItemType) { ... }
    fn visit_item_union_mut(&mut self, i: &mut ItemUnion) { ... }
    fn visit_item_use_mut(&mut self, i: &mut ItemUse) { ... }
    fn visit_label_mut(&mut self, i: &mut Label) { ... }
    fn visit_lifetime_mut(&mut self, i: &mut Lifetime) { ... }
    fn visit_lifetime_param_mut(&mut self, i: &mut LifetimeParam) { ... }
    fn visit_lit_mut(&mut self, i: &mut Lit) { ... }
    fn visit_lit_bool_mut(&mut self, i: &mut LitBool) { ... }
    fn visit_lit_byte_mut(&mut self, i: &mut LitByte) { ... }
    fn visit_lit_byte_str_mut(&mut self, i: &mut LitByteStr) { ... }
    fn visit_lit_cstr_mut(&mut self, i: &mut LitCStr) { ... }
    fn visit_lit_char_mut(&mut self, i: &mut LitChar) { ... }
    fn visit_lit_float_mut(&mut self, i: &mut LitFloat) { ... }
    fn visit_lit_int_mut(&mut self, i: &mut LitInt) { ... }
    fn visit_lit_str_mut(&mut self, i: &mut LitStr) { ... }
    fn visit_local_mut(&mut self, i: &mut Local) { ... }
    fn visit_local_init_mut(&mut self, i: &mut LocalInit) { ... }
    fn visit_macro_mut(&mut self, i: &mut Macro) { ... }
    fn visit_macro_delimiter_mut(&mut self, i: &mut MacroDelimiter) { ... }
    fn visit_member_mut(&mut self, i: &mut Member) { ... }
    fn visit_meta_mut(&mut self, i: &mut Meta) { ... }
    fn visit_meta_list_mut(&mut self, i: &mut MetaList) { ... }
    fn visit_meta_name_value_mut(&mut self, i: &mut MetaNameValue) { ... }
    fn visit_parenthesized_generic_arguments_mut(
        &mut self,
        i: &mut ParenthesizedGenericArguments,
    ) { ... }
    fn visit_pat_mut(&mut self, i: &mut Pat) { ... }
    fn visit_pat_ident_mut(&mut self, i: &mut PatIdent) { ... }
    fn visit_pat_or_mut(&mut self, i: &mut PatOr) { ... }
    fn visit_pat_paren_mut(&mut self, i: &mut PatParen) { ... }
    fn visit_pat_reference_mut(&mut self, i: &mut PatReference) { ... }
    fn visit_pat_rest_mut(&mut self, i: &mut PatRest) { ... }
    fn visit_pat_slice_mut(&mut self, i: &mut PatSlice) { ... }
    fn visit_pat_struct_mut(&mut self, i: &mut PatStruct) { ... }
    fn visit_pat_tuple_mut(&mut self, i: &mut PatTuple) { ... }
    fn visit_pat_tuple_struct_mut(&mut self, i: &mut PatTupleStruct) { ... }
    fn visit_pat_type_mut(&mut self, i: &mut PatType) { ... }
    fn visit_pat_wild_mut(&mut self, i: &mut PatWild) { ... }
    fn visit_path_mut(&mut self, i: &mut Path) { ... }
    fn visit_path_arguments_mut(&mut self, i: &mut PathArguments) { ... }
    fn visit_path_segment_mut(&mut self, i: &mut PathSegment) { ... }
    fn visit_pointer_mutability_mut(&mut self, i: &mut PointerMutability) { ... }
    fn visit_precise_capture_mut(&mut self, i: &mut PreciseCapture) { ... }
    fn visit_predicate_lifetime_mut(&mut self, i: &mut PredicateLifetime) { ... }
    fn visit_predicate_type_mut(&mut self, i: &mut PredicateType) { ... }
    fn visit_qself_mut(&mut self, i: &mut QSelf) { ... }
    fn visit_range_limits_mut(&mut self, i: &mut RangeLimits) { ... }
    fn visit_receiver_mut(&mut self, i: &mut Receiver) { ... }
    fn visit_return_type_mut(&mut self, i: &mut ReturnType) { ... }
    fn visit_signature_mut(&mut self, i: &mut Signature) { ... }
    fn visit_span_mut(&mut self, i: &mut Span) { ... }
    fn visit_static_mutability_mut(&mut self, i: &mut StaticMutability) { ... }
    fn visit_stmt_mut(&mut self, i: &mut Stmt) { ... }
    fn visit_stmt_macro_mut(&mut self, i: &mut StmtMacro) { ... }
    fn visit_token_stream_mut(&mut self, i: &mut TokenStream) { ... }
    fn visit_trait_bound_mut(&mut self, i: &mut TraitBound) { ... }
    fn visit_trait_bound_modifier_mut(&mut self, i: &mut TraitBoundModifier) { ... }
    fn visit_trait_item_mut(&mut self, i: &mut TraitItem) { ... }
    fn visit_trait_item_const_mut(&mut self, i: &mut TraitItemConst) { ... }
    fn visit_trait_item_fn_mut(&mut self, i: &mut TraitItemFn) { ... }
    fn visit_trait_item_macro_mut(&mut self, i: &mut TraitItemMacro) { ... }
    fn visit_trait_item_type_mut(&mut self, i: &mut TraitItemType) { ... }
    fn visit_type_mut(&mut self, i: &mut Type) { ... }
    fn visit_type_array_mut(&mut self, i: &mut TypeArray) { ... }
    fn visit_type_bare_fn_mut(&mut self, i: &mut TypeBareFn) { ... }
    fn visit_type_group_mut(&mut self, i: &mut TypeGroup) { ... }
    fn visit_type_impl_trait_mut(&mut self, i: &mut TypeImplTrait) { ... }
    fn visit_type_infer_mut(&mut self, i: &mut TypeInfer) { ... }
    fn visit_type_macro_mut(&mut self, i: &mut TypeMacro) { ... }
    fn visit_type_never_mut(&mut self, i: &mut TypeNever) { ... }
    fn visit_type_param_mut(&mut self, i: &mut TypeParam) { ... }
    fn visit_type_param_bound_mut(&mut self, i: &mut TypeParamBound) { ... }
    fn visit_type_paren_mut(&mut self, i: &mut TypeParen) { ... }
    fn visit_type_path_mut(&mut self, i: &mut TypePath) { ... }
    fn visit_type_ptr_mut(&mut self, i: &mut TypePtr) { ... }
    fn visit_type_reference_mut(&mut self, i: &mut TypeReference) { ... }
    fn visit_type_slice_mut(&mut self, i: &mut TypeSlice) { ... }
    fn visit_type_trait_object_mut(&mut self, i: &mut TypeTraitObject) { ... }
    fn visit_type_tuple_mut(&mut self, i: &mut TypeTuple) { ... }
    fn visit_un_op_mut(&mut self, i: &mut UnOp) { ... }
    fn visit_use_glob_mut(&mut self, i: &mut UseGlob) { ... }
    fn visit_use_group_mut(&mut self, i: &mut UseGroup) { ... }
    fn visit_use_name_mut(&mut self, i: &mut UseName) { ... }
    fn visit_use_path_mut(&mut self, i: &mut UsePath) { ... }
    fn visit_use_rename_mut(&mut self, i: &mut UseRename) { ... }
    fn visit_use_tree_mut(&mut self, i: &mut UseTree) { ... }
    fn visit_variadic_mut(&mut self, i: &mut Variadic) { ... }
    fn visit_variant_mut(&mut self, i: &mut Variant) { ... }
    fn visit_vis_restricted_mut(&mut self, i: &mut VisRestricted) { ... }
    fn visit_visibility_mut(&mut self, i: &mut Visibility) { ... }
    fn visit_where_clause_mut(&mut self, i: &mut WhereClause) { ... }
    fn visit_where_predicate_mut(&mut self, i: &mut WherePredicate) { ... }
}
```

Expand description

<div class="docblock">

Syntax tree traversal to mutate an exclusive borrow of a syntax tree in
place.

See the [module documentation](index.html "mod syn::visit_mut") for
details.

</div>

## Provided Methods<a href="#provided-methods" class="anchor">§</a>

<div class="methods">

<div id="method.visit_abi_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#34-36"
class="src rightside">Source</a>

#### fn <a href="#method.visit_abi_mut" class="fn">visit_abi_mut</a>(&mut self, i: &mut <a href="../struct.Abi.html" class="struct"
title="struct syn::Abi">Abi</a>)

</div>

<div id="method.visit_angle_bracketed_generic_arguments_mut"
class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#39-44"
class="src rightside">Source</a>

#### fn <a href="#method.visit_angle_bracketed_generic_arguments_mut"
class="fn">visit_angle_bracketed_generic_arguments_mut</a>( &mut self, i: &mut <a href="../struct.AngleBracketedGenericArguments.html" class="struct"
title="struct syn::AngleBracketedGenericArguments">AngleBracketedGenericArguments</a>, )

</div>

<div id="method.visit_arm_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#47-49"
class="src rightside">Source</a>

#### fn <a href="#method.visit_arm_mut" class="fn">visit_arm_mut</a>(&mut self, i: &mut <a href="../struct.Arm.html" class="struct"
title="struct syn::Arm">Arm</a>)

</div>

<div id="method.visit_assoc_const_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#52-54"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assoc_const_mut"
class="fn">visit_assoc_const_mut</a>(&mut self, i: &mut <a href="../struct.AssocConst.html" class="struct"
title="struct syn::AssocConst">AssocConst</a>)

</div>

<div id="method.visit_assoc_type_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#57-59"
class="src rightside">Source</a>

#### fn <a href="#method.visit_assoc_type_mut"
class="fn">visit_assoc_type_mut</a>(&mut self, i: &mut <a href="../struct.AssocType.html" class="struct"
title="struct syn::AssocType">AssocType</a>)

</div>

<div id="method.visit_attr_style_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#62-64"
class="src rightside">Source</a>

#### fn <a href="#method.visit_attr_style_mut"
class="fn">visit_attr_style_mut</a>(&mut self, i: &mut <a href="../enum.AttrStyle.html" class="enum"
title="enum syn::AttrStyle">AttrStyle</a>)

</div>

<div id="method.visit_attribute_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#67-69"
class="src rightside">Source</a>

#### fn <a href="#method.visit_attribute_mut" class="fn">visit_attribute_mut</a>(&mut self, i: &mut <a href="../struct.Attribute.html" class="struct"
title="struct syn::Attribute">Attribute</a>)

</div>

<div id="method.visit_attributes_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#72-76"
class="src rightside">Source</a>

#### fn <a href="#method.visit_attributes_mut"
class="fn">visit_attributes_mut</a>(&mut self, i: &mut <a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<<a href="../struct.Attribute.html" class="struct"
title="struct syn::Attribute">Attribute</a>\>)

</div>

<div id="method.visit_bare_fn_arg_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#79-81"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bare_fn_arg_mut"
class="fn">visit_bare_fn_arg_mut</a>(&mut self, i: &mut <a href="../struct.BareFnArg.html" class="struct"
title="struct syn::BareFnArg">BareFnArg</a>)

</div>

<div id="method.visit_bare_variadic_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#84-86"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bare_variadic_mut"
class="fn">visit_bare_variadic_mut</a>(&mut self, i: &mut <a href="../struct.BareVariadic.html" class="struct"
title="struct syn::BareVariadic">BareVariadic</a>)

</div>

<div id="method.visit_bin_op_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#89-91"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bin_op_mut" class="fn">visit_bin_op_mut</a>(&mut self, i: &mut <a href="../enum.BinOp.html" class="enum"
title="enum syn::BinOp">BinOp</a>)

</div>

<div id="method.visit_block_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#94-96"
class="src rightside">Source</a>

#### fn <a href="#method.visit_block_mut" class="fn">visit_block_mut</a>(&mut self, i: &mut <a href="../struct.Block.html" class="struct"
title="struct syn::Block">Block</a>)

</div>

<div id="method.visit_bound_lifetimes_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#99-101"
class="src rightside">Source</a>

#### fn <a href="#method.visit_bound_lifetimes_mut"
class="fn">visit_bound_lifetimes_mut</a>(&mut self, i: &mut <a href="../struct.BoundLifetimes.html" class="struct"
title="struct syn::BoundLifetimes">BoundLifetimes</a>)

</div>

<div id="method.visit_captured_param_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#104-106"
class="src rightside">Source</a>

#### fn <a href="#method.visit_captured_param_mut"
class="fn">visit_captured_param_mut</a>(&mut self, i: &mut <a href="../enum.CapturedParam.html" class="enum"
title="enum syn::CapturedParam">CapturedParam</a>)

</div>

<div id="method.visit_const_param_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#109-111"
class="src rightside">Source</a>

#### fn <a href="#method.visit_const_param_mut"
class="fn">visit_const_param_mut</a>(&mut self, i: &mut <a href="../struct.ConstParam.html" class="struct"
title="struct syn::ConstParam">ConstParam</a>)

</div>

<div id="method.visit_constraint_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#114-116"
class="src rightside">Source</a>

#### fn <a href="#method.visit_constraint_mut"
class="fn">visit_constraint_mut</a>(&mut self, i: &mut <a href="../struct.Constraint.html" class="struct"
title="struct syn::Constraint">Constraint</a>)

</div>

<div id="method.visit_data_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#119-121"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_mut" class="fn">visit_data_mut</a>(&mut self, i: &mut <a href="../enum.Data.html" class="enum" title="enum syn::Data">Data</a>)

</div>

<div id="method.visit_data_enum_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#124-126"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_enum_mut" class="fn">visit_data_enum_mut</a>(&mut self, i: &mut <a href="../struct.DataEnum.html" class="struct"
title="struct syn::DataEnum">DataEnum</a>)

</div>

<div id="method.visit_data_struct_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#129-131"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_struct_mut"
class="fn">visit_data_struct_mut</a>(&mut self, i: &mut <a href="../struct.DataStruct.html" class="struct"
title="struct syn::DataStruct">DataStruct</a>)

</div>

<div id="method.visit_data_union_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#134-136"
class="src rightside">Source</a>

#### fn <a href="#method.visit_data_union_mut"
class="fn">visit_data_union_mut</a>(&mut self, i: &mut <a href="../struct.DataUnion.html" class="struct"
title="struct syn::DataUnion">DataUnion</a>)

</div>

<div id="method.visit_derive_input_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#139-141"
class="src rightside">Source</a>

#### fn <a href="#method.visit_derive_input_mut"
class="fn">visit_derive_input_mut</a>(&mut self, i: &mut <a href="../struct.DeriveInput.html" class="struct"
title="struct syn::DeriveInput">DeriveInput</a>)

</div>

<div id="method.visit_expr_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#144-146"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_mut" class="fn">visit_expr_mut</a>(&mut self, i: &mut <a href="../enum.Expr.html" class="enum" title="enum syn::Expr">Expr</a>)

</div>

<div id="method.visit_expr_array_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#149-151"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_array_mut"
class="fn">visit_expr_array_mut</a>(&mut self, i: &mut <a href="../struct.ExprArray.html" class="struct"
title="struct syn::ExprArray">ExprArray</a>)

</div>

<div id="method.visit_expr_assign_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#154-156"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_assign_mut"
class="fn">visit_expr_assign_mut</a>(&mut self, i: &mut <a href="../struct.ExprAssign.html" class="struct"
title="struct syn::ExprAssign">ExprAssign</a>)

</div>

<div id="method.visit_expr_async_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#159-161"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_async_mut"
class="fn">visit_expr_async_mut</a>(&mut self, i: &mut <a href="../struct.ExprAsync.html" class="struct"
title="struct syn::ExprAsync">ExprAsync</a>)

</div>

<div id="method.visit_expr_await_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#164-166"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_await_mut"
class="fn">visit_expr_await_mut</a>(&mut self, i: &mut <a href="../struct.ExprAwait.html" class="struct"
title="struct syn::ExprAwait">ExprAwait</a>)

</div>

<div id="method.visit_expr_binary_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#169-171"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_binary_mut"
class="fn">visit_expr_binary_mut</a>(&mut self, i: &mut <a href="../struct.ExprBinary.html" class="struct"
title="struct syn::ExprBinary">ExprBinary</a>)

</div>

<div id="method.visit_expr_block_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#174-176"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_block_mut"
class="fn">visit_expr_block_mut</a>(&mut self, i: &mut <a href="../struct.ExprBlock.html" class="struct"
title="struct syn::ExprBlock">ExprBlock</a>)

</div>

<div id="method.visit_expr_break_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#179-181"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_break_mut"
class="fn">visit_expr_break_mut</a>(&mut self, i: &mut <a href="../struct.ExprBreak.html" class="struct"
title="struct syn::ExprBreak">ExprBreak</a>)

</div>

<div id="method.visit_expr_call_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#184-186"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_call_mut" class="fn">visit_expr_call_mut</a>(&mut self, i: &mut <a href="../struct.ExprCall.html" class="struct"
title="struct syn::ExprCall">ExprCall</a>)

</div>

<div id="method.visit_expr_cast_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#189-191"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_cast_mut" class="fn">visit_expr_cast_mut</a>(&mut self, i: &mut <a href="../struct.ExprCast.html" class="struct"
title="struct syn::ExprCast">ExprCast</a>)

</div>

<div id="method.visit_expr_closure_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#194-196"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_closure_mut"
class="fn">visit_expr_closure_mut</a>(&mut self, i: &mut <a href="../struct.ExprClosure.html" class="struct"
title="struct syn::ExprClosure">ExprClosure</a>)

</div>

<div id="method.visit_expr_const_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#199-201"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_const_mut"
class="fn">visit_expr_const_mut</a>(&mut self, i: &mut <a href="../struct.ExprConst.html" class="struct"
title="struct syn::ExprConst">ExprConst</a>)

</div>

<div id="method.visit_expr_continue_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#204-206"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_continue_mut"
class="fn">visit_expr_continue_mut</a>(&mut self, i: &mut <a href="../struct.ExprContinue.html" class="struct"
title="struct syn::ExprContinue">ExprContinue</a>)

</div>

<div id="method.visit_expr_field_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#209-211"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_field_mut"
class="fn">visit_expr_field_mut</a>(&mut self, i: &mut <a href="../struct.ExprField.html" class="struct"
title="struct syn::ExprField">ExprField</a>)

</div>

<div id="method.visit_expr_for_loop_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#214-216"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_for_loop_mut"
class="fn">visit_expr_for_loop_mut</a>(&mut self, i: &mut <a href="../struct.ExprForLoop.html" class="struct"
title="struct syn::ExprForLoop">ExprForLoop</a>)

</div>

<div id="method.visit_expr_group_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#219-221"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_group_mut"
class="fn">visit_expr_group_mut</a>(&mut self, i: &mut <a href="../struct.ExprGroup.html" class="struct"
title="struct syn::ExprGroup">ExprGroup</a>)

</div>

<div id="method.visit_expr_if_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#224-226"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_if_mut" class="fn">visit_expr_if_mut</a>(&mut self, i: &mut <a href="../struct.ExprIf.html" class="struct"
title="struct syn::ExprIf">ExprIf</a>)

</div>

<div id="method.visit_expr_index_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#229-231"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_index_mut"
class="fn">visit_expr_index_mut</a>(&mut self, i: &mut <a href="../struct.ExprIndex.html" class="struct"
title="struct syn::ExprIndex">ExprIndex</a>)

</div>

<div id="method.visit_expr_infer_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#234-236"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_infer_mut"
class="fn">visit_expr_infer_mut</a>(&mut self, i: &mut <a href="../struct.ExprInfer.html" class="struct"
title="struct syn::ExprInfer">ExprInfer</a>)

</div>

<div id="method.visit_expr_let_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#239-241"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_let_mut" class="fn">visit_expr_let_mut</a>(&mut self, i: &mut <a href="../struct.ExprLet.html" class="struct"
title="struct syn::ExprLet">ExprLet</a>)

</div>

<div id="method.visit_expr_lit_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#244-246"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_lit_mut" class="fn">visit_expr_lit_mut</a>(&mut self, i: &mut <a href="../struct.ExprLit.html" class="struct"
title="struct syn::ExprLit">ExprLit</a>)

</div>

<div id="method.visit_expr_loop_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#249-251"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_loop_mut" class="fn">visit_expr_loop_mut</a>(&mut self, i: &mut <a href="../struct.ExprLoop.html" class="struct"
title="struct syn::ExprLoop">ExprLoop</a>)

</div>

<div id="method.visit_expr_macro_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#254-256"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_macro_mut"
class="fn">visit_expr_macro_mut</a>(&mut self, i: &mut <a href="../struct.ExprMacro.html" class="struct"
title="struct syn::ExprMacro">ExprMacro</a>)

</div>

<div id="method.visit_expr_match_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#259-261"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_match_mut"
class="fn">visit_expr_match_mut</a>(&mut self, i: &mut <a href="../struct.ExprMatch.html" class="struct"
title="struct syn::ExprMatch">ExprMatch</a>)

</div>

<div id="method.visit_expr_method_call_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#264-266"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_method_call_mut"
class="fn">visit_expr_method_call_mut</a>(&mut self, i: &mut <a href="../struct.ExprMethodCall.html" class="struct"
title="struct syn::ExprMethodCall">ExprMethodCall</a>)

</div>

<div id="method.visit_expr_paren_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#269-271"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_paren_mut"
class="fn">visit_expr_paren_mut</a>(&mut self, i: &mut <a href="../struct.ExprParen.html" class="struct"
title="struct syn::ExprParen">ExprParen</a>)

</div>

<div id="method.visit_expr_path_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#274-276"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_path_mut" class="fn">visit_expr_path_mut</a>(&mut self, i: &mut <a href="../struct.ExprPath.html" class="struct"
title="struct syn::ExprPath">ExprPath</a>)

</div>

<div id="method.visit_expr_range_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#279-281"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_range_mut"
class="fn">visit_expr_range_mut</a>(&mut self, i: &mut <a href="../struct.ExprRange.html" class="struct"
title="struct syn::ExprRange">ExprRange</a>)

</div>

<div id="method.visit_expr_raw_addr_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#284-286"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_raw_addr_mut"
class="fn">visit_expr_raw_addr_mut</a>(&mut self, i: &mut <a href="../struct.ExprRawAddr.html" class="struct"
title="struct syn::ExprRawAddr">ExprRawAddr</a>)

</div>

<div id="method.visit_expr_reference_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#289-291"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_reference_mut"
class="fn">visit_expr_reference_mut</a>(&mut self, i: &mut <a href="../struct.ExprReference.html" class="struct"
title="struct syn::ExprReference">ExprReference</a>)

</div>

<div id="method.visit_expr_repeat_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#294-296"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_repeat_mut"
class="fn">visit_expr_repeat_mut</a>(&mut self, i: &mut <a href="../struct.ExprRepeat.html" class="struct"
title="struct syn::ExprRepeat">ExprRepeat</a>)

</div>

<div id="method.visit_expr_return_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#299-301"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_return_mut"
class="fn">visit_expr_return_mut</a>(&mut self, i: &mut <a href="../struct.ExprReturn.html" class="struct"
title="struct syn::ExprReturn">ExprReturn</a>)

</div>

<div id="method.visit_expr_struct_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#304-306"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_struct_mut"
class="fn">visit_expr_struct_mut</a>(&mut self, i: &mut <a href="../struct.ExprStruct.html" class="struct"
title="struct syn::ExprStruct">ExprStruct</a>)

</div>

<div id="method.visit_expr_try_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#309-311"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_try_mut" class="fn">visit_expr_try_mut</a>(&mut self, i: &mut <a href="../struct.ExprTry.html" class="struct"
title="struct syn::ExprTry">ExprTry</a>)

</div>

<div id="method.visit_expr_try_block_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#314-316"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_try_block_mut"
class="fn">visit_expr_try_block_mut</a>(&mut self, i: &mut <a href="../struct.ExprTryBlock.html" class="struct"
title="struct syn::ExprTryBlock">ExprTryBlock</a>)

</div>

<div id="method.visit_expr_tuple_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#319-321"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_tuple_mut"
class="fn">visit_expr_tuple_mut</a>(&mut self, i: &mut <a href="../struct.ExprTuple.html" class="struct"
title="struct syn::ExprTuple">ExprTuple</a>)

</div>

<div id="method.visit_expr_unary_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#324-326"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_unary_mut"
class="fn">visit_expr_unary_mut</a>(&mut self, i: &mut <a href="../struct.ExprUnary.html" class="struct"
title="struct syn::ExprUnary">ExprUnary</a>)

</div>

<div id="method.visit_expr_unsafe_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#329-331"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_unsafe_mut"
class="fn">visit_expr_unsafe_mut</a>(&mut self, i: &mut <a href="../struct.ExprUnsafe.html" class="struct"
title="struct syn::ExprUnsafe">ExprUnsafe</a>)

</div>

<div id="method.visit_expr_while_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#334-336"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_while_mut"
class="fn">visit_expr_while_mut</a>(&mut self, i: &mut <a href="../struct.ExprWhile.html" class="struct"
title="struct syn::ExprWhile">ExprWhile</a>)

</div>

<div id="method.visit_expr_yield_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#339-341"
class="src rightside">Source</a>

#### fn <a href="#method.visit_expr_yield_mut"
class="fn">visit_expr_yield_mut</a>(&mut self, i: &mut <a href="../struct.ExprYield.html" class="struct"
title="struct syn::ExprYield">ExprYield</a>)

</div>

<div id="method.visit_field_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#344-346"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_mut" class="fn">visit_field_mut</a>(&mut self, i: &mut <a href="../struct.Field.html" class="struct"
title="struct syn::Field">Field</a>)

</div>

<div id="method.visit_field_mutability_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#349-351"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_mutability_mut"
class="fn">visit_field_mutability_mut</a>(&mut self, i: &mut <a href="../enum.FieldMutability.html" class="enum"
title="enum syn::FieldMutability">FieldMutability</a>)

</div>

<div id="method.visit_field_pat_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#354-356"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_pat_mut" class="fn">visit_field_pat_mut</a>(&mut self, i: &mut <a href="../struct.FieldPat.html" class="struct"
title="struct syn::FieldPat">FieldPat</a>)

</div>

<div id="method.visit_field_value_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#359-361"
class="src rightside">Source</a>

#### fn <a href="#method.visit_field_value_mut"
class="fn">visit_field_value_mut</a>(&mut self, i: &mut <a href="../struct.FieldValue.html" class="struct"
title="struct syn::FieldValue">FieldValue</a>)

</div>

<div id="method.visit_fields_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#364-366"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fields_mut" class="fn">visit_fields_mut</a>(&mut self, i: &mut <a href="../enum.Fields.html" class="enum"
title="enum syn::Fields">Fields</a>)

</div>

<div id="method.visit_fields_named_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#369-371"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fields_named_mut"
class="fn">visit_fields_named_mut</a>(&mut self, i: &mut <a href="../struct.FieldsNamed.html" class="struct"
title="struct syn::FieldsNamed">FieldsNamed</a>)

</div>

<div id="method.visit_fields_unnamed_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#374-376"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fields_unnamed_mut"
class="fn">visit_fields_unnamed_mut</a>(&mut self, i: &mut <a href="../struct.FieldsUnnamed.html" class="struct"
title="struct syn::FieldsUnnamed">FieldsUnnamed</a>)

</div>

<div id="method.visit_file_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#379-381"
class="src rightside">Source</a>

#### fn <a href="#method.visit_file_mut" class="fn">visit_file_mut</a>(&mut self, i: &mut <a href="../struct.File.html" class="struct"
title="struct syn::File">File</a>)

</div>

<div id="method.visit_fn_arg_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#384-386"
class="src rightside">Source</a>

#### fn <a href="#method.visit_fn_arg_mut" class="fn">visit_fn_arg_mut</a>(&mut self, i: &mut <a href="../enum.FnArg.html" class="enum"
title="enum syn::FnArg">FnArg</a>)

</div>

<div id="method.visit_foreign_item_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#389-391"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_mut"
class="fn">visit_foreign_item_mut</a>(&mut self, i: &mut <a href="../enum.ForeignItem.html" class="enum"
title="enum syn::ForeignItem">ForeignItem</a>)

</div>

<div id="method.visit_foreign_item_fn_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#394-396"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_fn_mut"
class="fn">visit_foreign_item_fn_mut</a>(&mut self, i: &mut <a href="../struct.ForeignItemFn.html" class="struct"
title="struct syn::ForeignItemFn">ForeignItemFn</a>)

</div>

<div id="method.visit_foreign_item_macro_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#399-401"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_macro_mut"
class="fn">visit_foreign_item_macro_mut</a>(&mut self, i: &mut <a href="../struct.ForeignItemMacro.html" class="struct"
title="struct syn::ForeignItemMacro">ForeignItemMacro</a>)

</div>

<div id="method.visit_foreign_item_static_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#404-406"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_static_mut"
class="fn">visit_foreign_item_static_mut</a>(&mut self, i: &mut <a href="../struct.ForeignItemStatic.html" class="struct"
title="struct syn::ForeignItemStatic">ForeignItemStatic</a>)

</div>

<div id="method.visit_foreign_item_type_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#409-411"
class="src rightside">Source</a>

#### fn <a href="#method.visit_foreign_item_type_mut"
class="fn">visit_foreign_item_type_mut</a>(&mut self, i: &mut <a href="../struct.ForeignItemType.html" class="struct"
title="struct syn::ForeignItemType">ForeignItemType</a>)

</div>

<div id="method.visit_generic_argument_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#414-416"
class="src rightside">Source</a>

#### fn <a href="#method.visit_generic_argument_mut"
class="fn">visit_generic_argument_mut</a>(&mut self, i: &mut <a href="../enum.GenericArgument.html" class="enum"
title="enum syn::GenericArgument">GenericArgument</a>)

</div>

<div id="method.visit_generic_param_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#419-421"
class="src rightside">Source</a>

#### fn <a href="#method.visit_generic_param_mut"
class="fn">visit_generic_param_mut</a>(&mut self, i: &mut <a href="../enum.GenericParam.html" class="enum"
title="enum syn::GenericParam">GenericParam</a>)

</div>

<div id="method.visit_generics_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#424-426"
class="src rightside">Source</a>

#### fn <a href="#method.visit_generics_mut" class="fn">visit_generics_mut</a>(&mut self, i: &mut <a href="../struct.Generics.html" class="struct"
title="struct syn::Generics">Generics</a>)

</div>

<div id="method.visit_ident_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#427-429"
class="src rightside">Source</a>

#### fn <a href="#method.visit_ident_mut" class="fn">visit_ident_mut</a>(&mut self, i: &mut <a href="../struct.Ident.html" class="struct"
title="struct syn::Ident">Ident</a>)

</div>

<div id="method.visit_impl_item_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#432-434"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_mut" class="fn">visit_impl_item_mut</a>(&mut self, i: &mut <a href="../enum.ImplItem.html" class="enum"
title="enum syn::ImplItem">ImplItem</a>)

</div>

<div id="method.visit_impl_item_const_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#437-439"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_const_mut"
class="fn">visit_impl_item_const_mut</a>(&mut self, i: &mut <a href="../struct.ImplItemConst.html" class="struct"
title="struct syn::ImplItemConst">ImplItemConst</a>)

</div>

<div id="method.visit_impl_item_fn_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#442-444"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_fn_mut"
class="fn">visit_impl_item_fn_mut</a>(&mut self, i: &mut <a href="../struct.ImplItemFn.html" class="struct"
title="struct syn::ImplItemFn">ImplItemFn</a>)

</div>

<div id="method.visit_impl_item_macro_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#447-449"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_macro_mut"
class="fn">visit_impl_item_macro_mut</a>(&mut self, i: &mut <a href="../struct.ImplItemMacro.html" class="struct"
title="struct syn::ImplItemMacro">ImplItemMacro</a>)

</div>

<div id="method.visit_impl_item_type_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#452-454"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_item_type_mut"
class="fn">visit_impl_item_type_mut</a>(&mut self, i: &mut <a href="../struct.ImplItemType.html" class="struct"
title="struct syn::ImplItemType">ImplItemType</a>)

</div>

<div id="method.visit_impl_restriction_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#457-459"
class="src rightside">Source</a>

#### fn <a href="#method.visit_impl_restriction_mut"
class="fn">visit_impl_restriction_mut</a>(&mut self, i: &mut <a href="../enum.ImplRestriction.html" class="enum"
title="enum syn::ImplRestriction">ImplRestriction</a>)

</div>

<div id="method.visit_index_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#462-464"
class="src rightside">Source</a>

#### fn <a href="#method.visit_index_mut" class="fn">visit_index_mut</a>(&mut self, i: &mut <a href="../struct.Index.html" class="struct"
title="struct syn::Index">Index</a>)

</div>

<div id="method.visit_item_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#467-469"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_mut" class="fn">visit_item_mut</a>(&mut self, i: &mut <a href="../enum.Item.html" class="enum" title="enum syn::Item">Item</a>)

</div>

<div id="method.visit_item_const_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#472-474"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_const_mut"
class="fn">visit_item_const_mut</a>(&mut self, i: &mut <a href="../struct.ItemConst.html" class="struct"
title="struct syn::ItemConst">ItemConst</a>)

</div>

<div id="method.visit_item_enum_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#477-479"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_enum_mut" class="fn">visit_item_enum_mut</a>(&mut self, i: &mut <a href="../struct.ItemEnum.html" class="struct"
title="struct syn::ItemEnum">ItemEnum</a>)

</div>

<div id="method.visit_item_extern_crate_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#482-484"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_extern_crate_mut"
class="fn">visit_item_extern_crate_mut</a>(&mut self, i: &mut <a href="../struct.ItemExternCrate.html" class="struct"
title="struct syn::ItemExternCrate">ItemExternCrate</a>)

</div>

<div id="method.visit_item_fn_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#487-489"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_fn_mut" class="fn">visit_item_fn_mut</a>(&mut self, i: &mut <a href="../struct.ItemFn.html" class="struct"
title="struct syn::ItemFn">ItemFn</a>)

</div>

<div id="method.visit_item_foreign_mod_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#492-494"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_foreign_mod_mut"
class="fn">visit_item_foreign_mod_mut</a>(&mut self, i: &mut <a href="../struct.ItemForeignMod.html" class="struct"
title="struct syn::ItemForeignMod">ItemForeignMod</a>)

</div>

<div id="method.visit_item_impl_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#497-499"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_impl_mut" class="fn">visit_item_impl_mut</a>(&mut self, i: &mut <a href="../struct.ItemImpl.html" class="struct"
title="struct syn::ItemImpl">ItemImpl</a>)

</div>

<div id="method.visit_item_macro_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#502-504"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_macro_mut"
class="fn">visit_item_macro_mut</a>(&mut self, i: &mut <a href="../struct.ItemMacro.html" class="struct"
title="struct syn::ItemMacro">ItemMacro</a>)

</div>

<div id="method.visit_item_mod_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#507-509"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_mod_mut" class="fn">visit_item_mod_mut</a>(&mut self, i: &mut <a href="../struct.ItemMod.html" class="struct"
title="struct syn::ItemMod">ItemMod</a>)

</div>

<div id="method.visit_item_static_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#512-514"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_static_mut"
class="fn">visit_item_static_mut</a>(&mut self, i: &mut <a href="../struct.ItemStatic.html" class="struct"
title="struct syn::ItemStatic">ItemStatic</a>)

</div>

<div id="method.visit_item_struct_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#517-519"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_struct_mut"
class="fn">visit_item_struct_mut</a>(&mut self, i: &mut <a href="../struct.ItemStruct.html" class="struct"
title="struct syn::ItemStruct">ItemStruct</a>)

</div>

<div id="method.visit_item_trait_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#522-524"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_trait_mut"
class="fn">visit_item_trait_mut</a>(&mut self, i: &mut <a href="../struct.ItemTrait.html" class="struct"
title="struct syn::ItemTrait">ItemTrait</a>)

</div>

<div id="method.visit_item_trait_alias_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#527-529"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_trait_alias_mut"
class="fn">visit_item_trait_alias_mut</a>(&mut self, i: &mut <a href="../struct.ItemTraitAlias.html" class="struct"
title="struct syn::ItemTraitAlias">ItemTraitAlias</a>)

</div>

<div id="method.visit_item_type_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#532-534"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_type_mut" class="fn">visit_item_type_mut</a>(&mut self, i: &mut <a href="../struct.ItemType.html" class="struct"
title="struct syn::ItemType">ItemType</a>)

</div>

<div id="method.visit_item_union_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#537-539"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_union_mut"
class="fn">visit_item_union_mut</a>(&mut self, i: &mut <a href="../struct.ItemUnion.html" class="struct"
title="struct syn::ItemUnion">ItemUnion</a>)

</div>

<div id="method.visit_item_use_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#542-544"
class="src rightside">Source</a>

#### fn <a href="#method.visit_item_use_mut" class="fn">visit_item_use_mut</a>(&mut self, i: &mut <a href="../struct.ItemUse.html" class="struct"
title="struct syn::ItemUse">ItemUse</a>)

</div>

<div id="method.visit_label_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#547-549"
class="src rightside">Source</a>

#### fn <a href="#method.visit_label_mut" class="fn">visit_label_mut</a>(&mut self, i: &mut <a href="../struct.Label.html" class="struct"
title="struct syn::Label">Label</a>)

</div>

<div id="method.visit_lifetime_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#550-552"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lifetime_mut" class="fn">visit_lifetime_mut</a>(&mut self, i: &mut <a href="../struct.Lifetime.html" class="struct"
title="struct syn::Lifetime">Lifetime</a>)

</div>

<div id="method.visit_lifetime_param_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#555-557"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lifetime_param_mut"
class="fn">visit_lifetime_param_mut</a>(&mut self, i: &mut <a href="../struct.LifetimeParam.html" class="struct"
title="struct syn::LifetimeParam">LifetimeParam</a>)

</div>

<div id="method.visit_lit_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#558-560"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_mut" class="fn">visit_lit_mut</a>(&mut self, i: &mut <a href="../enum.Lit.html" class="enum" title="enum syn::Lit">Lit</a>)

</div>

<div id="method.visit_lit_bool_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#561-563"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_bool_mut" class="fn">visit_lit_bool_mut</a>(&mut self, i: &mut <a href="../struct.LitBool.html" class="struct"
title="struct syn::LitBool">LitBool</a>)

</div>

<div id="method.visit_lit_byte_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#564-566"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_byte_mut" class="fn">visit_lit_byte_mut</a>(&mut self, i: &mut <a href="../struct.LitByte.html" class="struct"
title="struct syn::LitByte">LitByte</a>)

</div>

<div id="method.visit_lit_byte_str_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#567-569"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_byte_str_mut"
class="fn">visit_lit_byte_str_mut</a>(&mut self, i: &mut <a href="../struct.LitByteStr.html" class="struct"
title="struct syn::LitByteStr">LitByteStr</a>)

</div>

<div id="method.visit_lit_cstr_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#570-572"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_cstr_mut" class="fn">visit_lit_cstr_mut</a>(&mut self, i: &mut <a href="../struct.LitCStr.html" class="struct"
title="struct syn::LitCStr">LitCStr</a>)

</div>

<div id="method.visit_lit_char_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#573-575"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_char_mut" class="fn">visit_lit_char_mut</a>(&mut self, i: &mut <a href="../struct.LitChar.html" class="struct"
title="struct syn::LitChar">LitChar</a>)

</div>

<div id="method.visit_lit_float_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#576-578"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_float_mut" class="fn">visit_lit_float_mut</a>(&mut self, i: &mut <a href="../struct.LitFloat.html" class="struct"
title="struct syn::LitFloat">LitFloat</a>)

</div>

<div id="method.visit_lit_int_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#579-581"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_int_mut" class="fn">visit_lit_int_mut</a>(&mut self, i: &mut <a href="../struct.LitInt.html" class="struct"
title="struct syn::LitInt">LitInt</a>)

</div>

<div id="method.visit_lit_str_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#582-584"
class="src rightside">Source</a>

#### fn <a href="#method.visit_lit_str_mut" class="fn">visit_lit_str_mut</a>(&mut self, i: &mut <a href="../struct.LitStr.html" class="struct"
title="struct syn::LitStr">LitStr</a>)

</div>

<div id="method.visit_local_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#587-589"
class="src rightside">Source</a>

#### fn <a href="#method.visit_local_mut" class="fn">visit_local_mut</a>(&mut self, i: &mut <a href="../struct.Local.html" class="struct"
title="struct syn::Local">Local</a>)

</div>

<div id="method.visit_local_init_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#592-594"
class="src rightside">Source</a>

#### fn <a href="#method.visit_local_init_mut"
class="fn">visit_local_init_mut</a>(&mut self, i: &mut <a href="../struct.LocalInit.html" class="struct"
title="struct syn::LocalInit">LocalInit</a>)

</div>

<div id="method.visit_macro_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#597-599"
class="src rightside">Source</a>

#### fn <a href="#method.visit_macro_mut" class="fn">visit_macro_mut</a>(&mut self, i: &mut <a href="../struct.Macro.html" class="struct"
title="struct syn::Macro">Macro</a>)

</div>

<div id="method.visit_macro_delimiter_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#602-604"
class="src rightside">Source</a>

#### fn <a href="#method.visit_macro_delimiter_mut"
class="fn">visit_macro_delimiter_mut</a>(&mut self, i: &mut <a href="../enum.MacroDelimiter.html" class="enum"
title="enum syn::MacroDelimiter">MacroDelimiter</a>)

</div>

<div id="method.visit_member_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#607-609"
class="src rightside">Source</a>

#### fn <a href="#method.visit_member_mut" class="fn">visit_member_mut</a>(&mut self, i: &mut <a href="../enum.Member.html" class="enum"
title="enum syn::Member">Member</a>)

</div>

<div id="method.visit_meta_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#612-614"
class="src rightside">Source</a>

#### fn <a href="#method.visit_meta_mut" class="fn">visit_meta_mut</a>(&mut self, i: &mut <a href="../enum.Meta.html" class="enum" title="enum syn::Meta">Meta</a>)

</div>

<div id="method.visit_meta_list_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#617-619"
class="src rightside">Source</a>

#### fn <a href="#method.visit_meta_list_mut" class="fn">visit_meta_list_mut</a>(&mut self, i: &mut <a href="../struct.MetaList.html" class="struct"
title="struct syn::MetaList">MetaList</a>)

</div>

<div id="method.visit_meta_name_value_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#622-624"
class="src rightside">Source</a>

#### fn <a href="#method.visit_meta_name_value_mut"
class="fn">visit_meta_name_value_mut</a>(&mut self, i: &mut <a href="../struct.MetaNameValue.html" class="struct"
title="struct syn::MetaNameValue">MetaNameValue</a>)

</div>

<div id="method.visit_parenthesized_generic_arguments_mut"
class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#627-632"
class="src rightside">Source</a>

#### fn <a href="#method.visit_parenthesized_generic_arguments_mut"
class="fn">visit_parenthesized_generic_arguments_mut</a>( &mut self, i: &mut <a href="../struct.ParenthesizedGenericArguments.html" class="struct"
title="struct syn::ParenthesizedGenericArguments">ParenthesizedGenericArguments</a>, )

</div>

<div id="method.visit_pat_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#635-637"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_mut" class="fn">visit_pat_mut</a>(&mut self, i: &mut <a href="../enum.Pat.html" class="enum" title="enum syn::Pat">Pat</a>)

</div>

<div id="method.visit_pat_ident_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#640-642"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_ident_mut" class="fn">visit_pat_ident_mut</a>(&mut self, i: &mut <a href="../struct.PatIdent.html" class="struct"
title="struct syn::PatIdent">PatIdent</a>)

</div>

<div id="method.visit_pat_or_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#645-647"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_or_mut" class="fn">visit_pat_or_mut</a>(&mut self, i: &mut <a href="../struct.PatOr.html" class="struct"
title="struct syn::PatOr">PatOr</a>)

</div>

<div id="method.visit_pat_paren_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#650-652"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_paren_mut" class="fn">visit_pat_paren_mut</a>(&mut self, i: &mut <a href="../struct.PatParen.html" class="struct"
title="struct syn::PatParen">PatParen</a>)

</div>

<div id="method.visit_pat_reference_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#655-657"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_reference_mut"
class="fn">visit_pat_reference_mut</a>(&mut self, i: &mut <a href="../struct.PatReference.html" class="struct"
title="struct syn::PatReference">PatReference</a>)

</div>

<div id="method.visit_pat_rest_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#660-662"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_rest_mut" class="fn">visit_pat_rest_mut</a>(&mut self, i: &mut <a href="../struct.PatRest.html" class="struct"
title="struct syn::PatRest">PatRest</a>)

</div>

<div id="method.visit_pat_slice_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#665-667"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_slice_mut" class="fn">visit_pat_slice_mut</a>(&mut self, i: &mut <a href="../struct.PatSlice.html" class="struct"
title="struct syn::PatSlice">PatSlice</a>)

</div>

<div id="method.visit_pat_struct_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#670-672"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_struct_mut"
class="fn">visit_pat_struct_mut</a>(&mut self, i: &mut <a href="../struct.PatStruct.html" class="struct"
title="struct syn::PatStruct">PatStruct</a>)

</div>

<div id="method.visit_pat_tuple_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#675-677"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_tuple_mut" class="fn">visit_pat_tuple_mut</a>(&mut self, i: &mut <a href="../struct.PatTuple.html" class="struct"
title="struct syn::PatTuple">PatTuple</a>)

</div>

<div id="method.visit_pat_tuple_struct_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#680-682"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_tuple_struct_mut"
class="fn">visit_pat_tuple_struct_mut</a>(&mut self, i: &mut <a href="../struct.PatTupleStruct.html" class="struct"
title="struct syn::PatTupleStruct">PatTupleStruct</a>)

</div>

<div id="method.visit_pat_type_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#685-687"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_type_mut" class="fn">visit_pat_type_mut</a>(&mut self, i: &mut <a href="../struct.PatType.html" class="struct"
title="struct syn::PatType">PatType</a>)

</div>

<div id="method.visit_pat_wild_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#690-692"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pat_wild_mut" class="fn">visit_pat_wild_mut</a>(&mut self, i: &mut <a href="../struct.PatWild.html" class="struct"
title="struct syn::PatWild">PatWild</a>)

</div>

<div id="method.visit_path_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#695-697"
class="src rightside">Source</a>

#### fn <a href="#method.visit_path_mut" class="fn">visit_path_mut</a>(&mut self, i: &mut <a href="../struct.Path.html" class="struct"
title="struct syn::Path">Path</a>)

</div>

<div id="method.visit_path_arguments_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#700-702"
class="src rightside">Source</a>

#### fn <a href="#method.visit_path_arguments_mut"
class="fn">visit_path_arguments_mut</a>(&mut self, i: &mut <a href="../enum.PathArguments.html" class="enum"
title="enum syn::PathArguments">PathArguments</a>)

</div>

<div id="method.visit_path_segment_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#705-707"
class="src rightside">Source</a>

#### fn <a href="#method.visit_path_segment_mut"
class="fn">visit_path_segment_mut</a>(&mut self, i: &mut <a href="../struct.PathSegment.html" class="struct"
title="struct syn::PathSegment">PathSegment</a>)

</div>

<div id="method.visit_pointer_mutability_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#710-712"
class="src rightside">Source</a>

#### fn <a href="#method.visit_pointer_mutability_mut"
class="fn">visit_pointer_mutability_mut</a>(&mut self, i: &mut <a href="../enum.PointerMutability.html" class="enum"
title="enum syn::PointerMutability">PointerMutability</a>)

</div>

<div id="method.visit_precise_capture_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#715-717"
class="src rightside">Source</a>

#### fn <a href="#method.visit_precise_capture_mut"
class="fn">visit_precise_capture_mut</a>(&mut self, i: &mut <a href="../struct.PreciseCapture.html" class="struct"
title="struct syn::PreciseCapture">PreciseCapture</a>)

</div>

<div id="method.visit_predicate_lifetime_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#720-722"
class="src rightside">Source</a>

#### fn <a href="#method.visit_predicate_lifetime_mut"
class="fn">visit_predicate_lifetime_mut</a>(&mut self, i: &mut <a href="../struct.PredicateLifetime.html" class="struct"
title="struct syn::PredicateLifetime">PredicateLifetime</a>)

</div>

<div id="method.visit_predicate_type_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#725-727"
class="src rightside">Source</a>

#### fn <a href="#method.visit_predicate_type_mut"
class="fn">visit_predicate_type_mut</a>(&mut self, i: &mut <a href="../struct.PredicateType.html" class="struct"
title="struct syn::PredicateType">PredicateType</a>)

</div>

<div id="method.visit_qself_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#730-732"
class="src rightside">Source</a>

#### fn <a href="#method.visit_qself_mut" class="fn">visit_qself_mut</a>(&mut self, i: &mut <a href="../struct.QSelf.html" class="struct"
title="struct syn::QSelf">QSelf</a>)

</div>

<div id="method.visit_range_limits_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#735-737"
class="src rightside">Source</a>

#### fn <a href="#method.visit_range_limits_mut"
class="fn">visit_range_limits_mut</a>(&mut self, i: &mut <a href="../enum.RangeLimits.html" class="enum"
title="enum syn::RangeLimits">RangeLimits</a>)

</div>

<div id="method.visit_receiver_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#740-742"
class="src rightside">Source</a>

#### fn <a href="#method.visit_receiver_mut" class="fn">visit_receiver_mut</a>(&mut self, i: &mut <a href="../struct.Receiver.html" class="struct"
title="struct syn::Receiver">Receiver</a>)

</div>

<div id="method.visit_return_type_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#745-747"
class="src rightside">Source</a>

#### fn <a href="#method.visit_return_type_mut"
class="fn">visit_return_type_mut</a>(&mut self, i: &mut <a href="../enum.ReturnType.html" class="enum"
title="enum syn::ReturnType">ReturnType</a>)

</div>

<div id="method.visit_signature_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#750-752"
class="src rightside">Source</a>

#### fn <a href="#method.visit_signature_mut" class="fn">visit_signature_mut</a>(&mut self, i: &mut <a href="../struct.Signature.html" class="struct"
title="struct syn::Signature">Signature</a>)

</div>

<div id="method.visit_span_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#753"
class="src rightside">Source</a>

#### fn <a href="#method.visit_span_mut" class="fn">visit_span_mut</a>(&mut self, i: &mut <a href="../../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>)

</div>

<div id="method.visit_static_mutability_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#756-758"
class="src rightside">Source</a>

#### fn <a href="#method.visit_static_mutability_mut"
class="fn">visit_static_mutability_mut</a>(&mut self, i: &mut <a href="../enum.StaticMutability.html" class="enum"
title="enum syn::StaticMutability">StaticMutability</a>)

</div>

<div id="method.visit_stmt_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#761-763"
class="src rightside">Source</a>

#### fn <a href="#method.visit_stmt_mut" class="fn">visit_stmt_mut</a>(&mut self, i: &mut <a href="../enum.Stmt.html" class="enum" title="enum syn::Stmt">Stmt</a>)

</div>

<div id="method.visit_stmt_macro_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#766-768"
class="src rightside">Source</a>

#### fn <a href="#method.visit_stmt_macro_mut"
class="fn">visit_stmt_macro_mut</a>(&mut self, i: &mut <a href="../struct.StmtMacro.html" class="struct"
title="struct syn::StmtMacro">StmtMacro</a>)

</div>

<div id="method.visit_token_stream_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#769"
class="src rightside">Source</a>

#### fn <a href="#method.visit_token_stream_mut"
class="fn">visit_token_stream_mut</a>(&mut self, i: &mut <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div id="method.visit_trait_bound_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#772-774"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_bound_mut"
class="fn">visit_trait_bound_mut</a>(&mut self, i: &mut <a href="../struct.TraitBound.html" class="struct"
title="struct syn::TraitBound">TraitBound</a>)

</div>

<div id="method.visit_trait_bound_modifier_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#777-779"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_bound_modifier_mut"
class="fn">visit_trait_bound_modifier_mut</a>(&mut self, i: &mut <a href="../enum.TraitBoundModifier.html" class="enum"
title="enum syn::TraitBoundModifier">TraitBoundModifier</a>)

</div>

<div id="method.visit_trait_item_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#782-784"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_mut"
class="fn">visit_trait_item_mut</a>(&mut self, i: &mut <a href="../enum.TraitItem.html" class="enum"
title="enum syn::TraitItem">TraitItem</a>)

</div>

<div id="method.visit_trait_item_const_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#787-789"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_const_mut"
class="fn">visit_trait_item_const_mut</a>(&mut self, i: &mut <a href="../struct.TraitItemConst.html" class="struct"
title="struct syn::TraitItemConst">TraitItemConst</a>)

</div>

<div id="method.visit_trait_item_fn_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#792-794"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_fn_mut"
class="fn">visit_trait_item_fn_mut</a>(&mut self, i: &mut <a href="../struct.TraitItemFn.html" class="struct"
title="struct syn::TraitItemFn">TraitItemFn</a>)

</div>

<div id="method.visit_trait_item_macro_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#797-799"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_macro_mut"
class="fn">visit_trait_item_macro_mut</a>(&mut self, i: &mut <a href="../struct.TraitItemMacro.html" class="struct"
title="struct syn::TraitItemMacro">TraitItemMacro</a>)

</div>

<div id="method.visit_trait_item_type_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#802-804"
class="src rightside">Source</a>

#### fn <a href="#method.visit_trait_item_type_mut"
class="fn">visit_trait_item_type_mut</a>(&mut self, i: &mut <a href="../struct.TraitItemType.html" class="struct"
title="struct syn::TraitItemType">TraitItemType</a>)

</div>

<div id="method.visit_type_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#807-809"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_mut" class="fn">visit_type_mut</a>(&mut self, i: &mut <a href="../enum.Type.html" class="enum" title="enum syn::Type">Type</a>)

</div>

<div id="method.visit_type_array_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#812-814"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_array_mut"
class="fn">visit_type_array_mut</a>(&mut self, i: &mut <a href="../struct.TypeArray.html" class="struct"
title="struct syn::TypeArray">TypeArray</a>)

</div>

<div id="method.visit_type_bare_fn_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#817-819"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_bare_fn_mut"
class="fn">visit_type_bare_fn_mut</a>(&mut self, i: &mut <a href="../struct.TypeBareFn.html" class="struct"
title="struct syn::TypeBareFn">TypeBareFn</a>)

</div>

<div id="method.visit_type_group_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#822-824"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_group_mut"
class="fn">visit_type_group_mut</a>(&mut self, i: &mut <a href="../struct.TypeGroup.html" class="struct"
title="struct syn::TypeGroup">TypeGroup</a>)

</div>

<div id="method.visit_type_impl_trait_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#827-829"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_impl_trait_mut"
class="fn">visit_type_impl_trait_mut</a>(&mut self, i: &mut <a href="../struct.TypeImplTrait.html" class="struct"
title="struct syn::TypeImplTrait">TypeImplTrait</a>)

</div>

<div id="method.visit_type_infer_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#832-834"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_infer_mut"
class="fn">visit_type_infer_mut</a>(&mut self, i: &mut <a href="../struct.TypeInfer.html" class="struct"
title="struct syn::TypeInfer">TypeInfer</a>)

</div>

<div id="method.visit_type_macro_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#837-839"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_macro_mut"
class="fn">visit_type_macro_mut</a>(&mut self, i: &mut <a href="../struct.TypeMacro.html" class="struct"
title="struct syn::TypeMacro">TypeMacro</a>)

</div>

<div id="method.visit_type_never_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#842-844"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_never_mut"
class="fn">visit_type_never_mut</a>(&mut self, i: &mut <a href="../struct.TypeNever.html" class="struct"
title="struct syn::TypeNever">TypeNever</a>)

</div>

<div id="method.visit_type_param_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#847-849"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_param_mut"
class="fn">visit_type_param_mut</a>(&mut self, i: &mut <a href="../struct.TypeParam.html" class="struct"
title="struct syn::TypeParam">TypeParam</a>)

</div>

<div id="method.visit_type_param_bound_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#852-854"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_param_bound_mut"
class="fn">visit_type_param_bound_mut</a>(&mut self, i: &mut <a href="../enum.TypeParamBound.html" class="enum"
title="enum syn::TypeParamBound">TypeParamBound</a>)

</div>

<div id="method.visit_type_paren_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#857-859"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_paren_mut"
class="fn">visit_type_paren_mut</a>(&mut self, i: &mut <a href="../struct.TypeParen.html" class="struct"
title="struct syn::TypeParen">TypeParen</a>)

</div>

<div id="method.visit_type_path_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#862-864"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_path_mut" class="fn">visit_type_path_mut</a>(&mut self, i: &mut <a href="../struct.TypePath.html" class="struct"
title="struct syn::TypePath">TypePath</a>)

</div>

<div id="method.visit_type_ptr_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#867-869"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_ptr_mut" class="fn">visit_type_ptr_mut</a>(&mut self, i: &mut <a href="../struct.TypePtr.html" class="struct"
title="struct syn::TypePtr">TypePtr</a>)

</div>

<div id="method.visit_type_reference_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#872-874"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_reference_mut"
class="fn">visit_type_reference_mut</a>(&mut self, i: &mut <a href="../struct.TypeReference.html" class="struct"
title="struct syn::TypeReference">TypeReference</a>)

</div>

<div id="method.visit_type_slice_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#877-879"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_slice_mut"
class="fn">visit_type_slice_mut</a>(&mut self, i: &mut <a href="../struct.TypeSlice.html" class="struct"
title="struct syn::TypeSlice">TypeSlice</a>)

</div>

<div id="method.visit_type_trait_object_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#882-884"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_trait_object_mut"
class="fn">visit_type_trait_object_mut</a>(&mut self, i: &mut <a href="../struct.TypeTraitObject.html" class="struct"
title="struct syn::TypeTraitObject">TypeTraitObject</a>)

</div>

<div id="method.visit_type_tuple_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#887-889"
class="src rightside">Source</a>

#### fn <a href="#method.visit_type_tuple_mut"
class="fn">visit_type_tuple_mut</a>(&mut self, i: &mut <a href="../struct.TypeTuple.html" class="struct"
title="struct syn::TypeTuple">TypeTuple</a>)

</div>

<div id="method.visit_un_op_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#892-894"
class="src rightside">Source</a>

#### fn <a href="#method.visit_un_op_mut" class="fn">visit_un_op_mut</a>(&mut self, i: &mut <a href="../enum.UnOp.html" class="enum" title="enum syn::UnOp">UnOp</a>)

</div>

<div id="method.visit_use_glob_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#897-899"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_glob_mut" class="fn">visit_use_glob_mut</a>(&mut self, i: &mut <a href="../struct.UseGlob.html" class="struct"
title="struct syn::UseGlob">UseGlob</a>)

</div>

<div id="method.visit_use_group_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#902-904"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_group_mut" class="fn">visit_use_group_mut</a>(&mut self, i: &mut <a href="../struct.UseGroup.html" class="struct"
title="struct syn::UseGroup">UseGroup</a>)

</div>

<div id="method.visit_use_name_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#907-909"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_name_mut" class="fn">visit_use_name_mut</a>(&mut self, i: &mut <a href="../struct.UseName.html" class="struct"
title="struct syn::UseName">UseName</a>)

</div>

<div id="method.visit_use_path_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#912-914"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_path_mut" class="fn">visit_use_path_mut</a>(&mut self, i: &mut <a href="../struct.UsePath.html" class="struct"
title="struct syn::UsePath">UsePath</a>)

</div>

<div id="method.visit_use_rename_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#917-919"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_rename_mut"
class="fn">visit_use_rename_mut</a>(&mut self, i: &mut <a href="../struct.UseRename.html" class="struct"
title="struct syn::UseRename">UseRename</a>)

</div>

<div id="method.visit_use_tree_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#922-924"
class="src rightside">Source</a>

#### fn <a href="#method.visit_use_tree_mut" class="fn">visit_use_tree_mut</a>(&mut self, i: &mut <a href="../enum.UseTree.html" class="enum"
title="enum syn::UseTree">UseTree</a>)

</div>

<div id="method.visit_variadic_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#927-929"
class="src rightside">Source</a>

#### fn <a href="#method.visit_variadic_mut" class="fn">visit_variadic_mut</a>(&mut self, i: &mut <a href="../struct.Variadic.html" class="struct"
title="struct syn::Variadic">Variadic</a>)

</div>

<div id="method.visit_variant_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#932-934"
class="src rightside">Source</a>

#### fn <a href="#method.visit_variant_mut" class="fn">visit_variant_mut</a>(&mut self, i: &mut <a href="../struct.Variant.html" class="struct"
title="struct syn::Variant">Variant</a>)

</div>

<div id="method.visit_vis_restricted_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#937-939"
class="src rightside">Source</a>

#### fn <a href="#method.visit_vis_restricted_mut"
class="fn">visit_vis_restricted_mut</a>(&mut self, i: &mut <a href="../struct.VisRestricted.html" class="struct"
title="struct syn::VisRestricted">VisRestricted</a>)

</div>

<div id="method.visit_visibility_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#942-944"
class="src rightside">Source</a>

#### fn <a href="#method.visit_visibility_mut"
class="fn">visit_visibility_mut</a>(&mut self, i: &mut <a href="../enum.Visibility.html" class="enum"
title="enum syn::Visibility">Visibility</a>)

</div>

<div id="method.visit_where_clause_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#947-949"
class="src rightside">Source</a>

#### fn <a href="#method.visit_where_clause_mut"
class="fn">visit_where_clause_mut</a>(&mut self, i: &mut <a href="../struct.WhereClause.html" class="struct"
title="struct syn::WhereClause">WhereClause</a>)

</div>

<div id="method.visit_where_predicate_mut" class="section method">

<a href="../../src/syn/gen/visit_mut.rs.html#952-954"
class="src rightside">Source</a>

#### fn <a href="#method.visit_where_predicate_mut"
class="fn">visit_where_predicate_mut</a>(&mut self, i: &mut <a href="../enum.WherePredicate.html" class="enum"
title="enum syn::WherePredicate">WherePredicate</a>)

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
