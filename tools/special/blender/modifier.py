############################################################################
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <https://www.gnu.org/licenses/>.
############################################################################

import bpy
from bpy.types import Operator
from bsmax.actions import modifier_add
from bsmax.state import is_objects_selected

class BsMax_OT_Lattice_2x2x2_Set(Operator):
	bl_idname = "modifier.lattice_2x2x2_set"
	bl_label = "Lattice 2x2x2 (Set)"
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		bpy.ops.lattice.set_on_selection(res_u=2,res_v=2,res_w=2)
		self.report({'INFO'},'bpy.ops.modifier.lattice_2x2x2_set()')
		return{"FINISHED"}

class BsMax_OT_Lattice_3x3x3_Set(Operator):
	bl_idname = "modifier.lattice_3x3x3_set"
	bl_label = "Lattice 3x3x3 (Set)"
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		bpy.ops.lattice.set_on_selection(res_u=3,res_v=3,res_w=3)
		self.report({'INFO'},'bpy.ops.modifier.lattice_3x3x3_set()')
		return{"FINISHED"}

class BsMax_OT_Lattice_4x4x4_Set(Operator):
	bl_idname = "modifier.lattice_4x4x4_set"
	bl_label = "Lattice 4x4x4 (Set)"
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		bpy.ops.lattice.set_on_selection(res_u=4,res_v=4,res_w=4)
		self.report({'INFO'},'bpy.ops.modifier.lattice_4x4x4_set()')
		return{"FINISHED"}

class BsMax_OT_DATA_TRANSFER_Add(Operator):
	bl_idname = "modifier.datatransformadd"
	bl_label = "Data Transfer (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'DATA_TRANSFER')
		self.report({'INFO'},'bpy.ops.modifier.datatransformadd()')
		return {'FINISHED'}

class BsMax_OT_MESH_CACHE_Add(Operator):
	bl_idname = "modifier.meshcacheadd"
	bl_label = "Mesh Cache (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'MESH_CACHE')
		self.report({'INFO'},'bpy.ops.modifier.meshcacheadd()')
		return {'FINISHED'}

class BsMax_OT_MESH_SEQUENCE_CACHE_Add(Operator):
	bl_idname = "modifier.meshsequencecacheadd"
	bl_label = "Mesh Sequence Cache (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'MESH_SEQUENCE_CACHE')
		self.report({'INFO'},'bpy.ops.modifier.meshsequencecacheadd()')
		return {'FINISHED'}

class BsMax_OT_NORMAL_EDIT_Add(Operator):
	bl_idname = "modifier.normaleditadd"
	bl_label = "Normal Edit (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'NORMAL_EDIT')
		self.report({'INFO'},'bpy.ops.modifier.normaleditadd()')
		return {'FINISHED'}

class BsMax_OT_WEIGHTED_NORMAL_Add(Operator):
	bl_idname = "modifier.weightednormaladd"
	bl_label = "Weighted Normal (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'WEIGHTED_NORMAL')
		self.report({'INFO'},'bpy.ops.modifier.weightednormaladd()')
		return {'FINISHED'}

class BsMax_OT_UV_PROJECT_Add(Operator):
	bl_idname = "modifier.uvprojectadd"
	bl_label = "UV Project (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'UV_PROJECT')
		self.report({'INFO'},'bpy.ops.modifier.uvprojectadd()')
		return {'FINISHED'}

class BsMax_OT_UV_WARP_Add(Operator):
	bl_idname = "modifier.uvwarpadd"
	bl_label = "UV Warp (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'UV_WARP')
		self.report({'INFO'},'bpy.ops.modifier.uvwarpadd()')
		return {'FINISHED'}

class BsMax_OT_VERTEX_WEIGHT_EDIT_Add(Operator):
	bl_idname = "modifier.vertexweighteditadd"
	bl_label = "Vertex Weight Edit (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'VERTEX_WEIGHT_EDIT')
		self.report({'INFO'},'bpy.ops.modifier.vertexweighteditadd()')
		return {'FINISHED'}

class BsMax_OT_VERTEX_WEIGHT_MIX_Add(Operator):
	bl_idname = "modifier.vertexweightmixadd"
	bl_label = "Vertex Weight Mix (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'VERTEX_WEIGHT_MIX')
		self.report({'INFO'},'bpy.ops.modifier.vertexweightmixadd()')
		return {'FINISHED'}

class BsMax_OT_VERTEX_WEIGHT_PROXIMITY_Add(Operator):
	bl_idname = "modifier.vertexweightproximityadd"
	bl_label = "Vertex Weight Proximity (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'VERTEX_WEIGHT_PROXIMITY')
		self.report({'INFO'},'bpy.ops.modifier.vertexweightproximityadd()')
		return {'FINISHED'}

class BsMax_OT_ARRAY_Add(Operator):
	bl_idname = "modifier.arrayadd"
	bl_label = "Array (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'ARRAY')
		self.report({'INFO'},'bpy.ops.modifier.arrayadd()')
		return {'FINISHED'}

class BsMax_OT_BEVEL_Add(Operator):
	bl_idname = "modifier.beveladd"
	bl_label = "Bevel (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'BEVEL')
		self.report({'INFO'},'bpy.ops.modifier.beveladd()')
		return {'FINISHED'}

class BsMax_OT_BOOLEAN_Add(Operator):
	bl_idname = "modifier.booleanadd"
	bl_label = "Boolean (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'BOOLEAN')
		self.report({'INFO'},'bpy.ops.modifier.booleanadd()')
		return {'FINISHED'}

class BsMax_OT_BUILD_Add(Operator):
	bl_idname = "modifier.buildadd"
	bl_label = "Build (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'BUILD')
		self.report({'INFO'},'bpy.ops.modifier.buildadd()')
		return {'FINISHED'}

class BsMax_OT_DECIMATE_Add(Operator):
	bl_idname = "modifier.decimateadd"
	bl_label = "Decimate (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'DECIMATE')
		self.report({'INFO'},'bpy.ops.modifier.decimateadd()')
		return {'FINISHED'}

class BsMax_OT_EDGE_SPLIT_Add(Operator):
	bl_idname = "modifier.edgesplitadd"
	bl_label = "Edge Split (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'EDGE_SPLIT')
		self.report({'INFO'},'bpy.ops.modifier.edgesplitadd()')
		return {'FINISHED'}

class BsMax_OT_Mask_Add(Operator):
	bl_idname = "modifier.maskadd"
	bl_label = "Mask (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'MASK')
		self.report({'INFO'},'bpy.ops.modifier.maskadd()')
		return {'FINISHED'}

class BsMax_OT_MIRROR_Add(Operator):
	bl_idname = "modifier.mirroradd"
	bl_label = "Mirror (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'MIRROR')
		self.report({'INFO'},'bpy.ops.modifier.mirroradd()')
		return {'FINISHED'}

class BsMax_OT_MULTIRES_Add(Operator):
	bl_idname = "modifier.multiresadd"
	bl_label = "Multires (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'MULTIRES')
		self.report({'INFO'},'bpy.ops.modifier.multiresadd()')
		return {'FINISHED'}

class BsMax_OT_REMESH_Add(Operator):
	bl_idname = "modifier.remeshadd"
	bl_label = "Remesh (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'REMESH')
		self.report({'INFO'},'bpy.ops.modifier.remeshadd()')
		return {'FINISHED'}

class BsMax_OT_Screw_Add(Operator):
	bl_idname = "modifier.screwadd"
	bl_label = "Screw (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'SCREW')
		self.report({'INFO'},'bpy.ops.modifier.screwadd()')
		return {'FINISHED'}

class BsMax_OT_SKIN_Add(Operator):
	bl_idname = "modifier.skinadd"
	bl_label = "Skin (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'SKIN')
		self.report({'INFO'},'bpy.ops.modifier.skinadd()')
		return {'FINISHED'}

class BsMax_OT_SOLIDIFY_Add(Operator):
	bl_idname = "modifier.solidifyadd"
	bl_label = "Solidify (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'SOLIDIFY')
		self.report({'INFO'},'bpy.ops.modifier.solidifyadd()')
		return {'FINISHED'}

class BsMax_OT_SUBSURF_Add(Operator):
	bl_idname = "modifier.subsurfadd"
	bl_label = "Subsurf (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'SUBSURF')
		self.report({'INFO'},'bpy.ops.modifier.subsurfadd()')
		return {'FINISHED'}

class BsMax_OT_TRIANGULATE_Add(Operator):
	bl_idname = "modifier.triangulateadd"
	bl_label = "Triangulate (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'TRIANGULATE')
		self.report({'INFO'},'bpy.ops.modifier.triangulateadd()')
		return {'FINISHED'}

class BsMax_OT_WIREFRAME_Add(Operator):
	bl_idname = "modifier.wireframeadd"
	bl_label = "Wireframe (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'WIREFRAME')
		self.report({'INFO'},'bpy.ops.modifier.wireframeadd()')
		return {'FINISHED'}

class BsMax_OT_ARMATURE_Add(Operator):
	bl_idname = "modifier.armatureadd"
	bl_label = "Armature (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'ARMATURE')
		self.report({'INFO'},'bpy.ops.modifier.armatureadd()')
		return {'FINISHED'}

class BsMax_OT_CAST_Add(Operator):
	bl_idname = "modifier.castadd"
	bl_label = "Cast (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'CAST')
		self.report({'INFO'},'bpy.ops.modifier.castadd()')
		return {'FINISHED'}

class BsMax_OT_CURVE_Add(Operator):
	bl_idname = "modifier.curveadd"
	bl_label = "Curve (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'CURVE')
		self.report({'INFO'},'bpy.ops.modifier.curveadd()')
		return {'FINISHED'}

class BsMax_OT_DISPLACE_Add(Operator):
	bl_idname = "modifier.displaceadd"
	bl_label = "Displace (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'DISPLACE')
		self.report({'INFO'},'bpy.ops.modifier.displaceadd()')
		return {'FINISHED'}

class BsMax_OT_HOOK_Add(Operator):
	bl_idname = "modifier.hookadd"
	bl_label = "Hook (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'HOOK')
		self.report({'INFO'},'bpy.ops.modifier.hookadd()')
		return {'FINISHED'}

class BsMax_OT_LAPLACIANDEFORM_Add(Operator):
	bl_idname = "modifier.laplaciandeformadd"
	bl_label = "Laplacian Deform (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'LAPLACIANDEFORM')
		self.report({'INFO'},'bpy.ops.modifier.laplaciandeformadd()')
		return {'FINISHED'}

class BsMax_OT_LATTICE_Add(Operator):
	bl_idname = "modifier.latticeadd"
	bl_label = "Lattice (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'LATTICE')
		self.report({'INFO'},'bpy.ops.modifier.latticeadd()')
		return {'FINISHED'}

class BsMax_OT_MESH_DEFORM_Add(Operator):
	bl_idname = "modifier.meshdeformadd"
	bl_label = "Mesh Deform (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'MESH_DEFORM')
		self.report({'INFO'},'bpy.ops.modifier.meshdeformadd()')
		return {'FINISHED'}

class BsMax_OT_SHRINKWRAP_Add(Operator):
	bl_idname = "modifier.shrinkwarpadd"
	bl_label = "Shrink Warp (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'SHRINKWRAP')
		self.report({'INFO'},'bpy.ops.modifier.shrinkwarpadd()')
		return {'FINISHED'}

class BsMax_OT_SIMPLE_DEFORM_Add(Operator):
	bl_idname = "modifier.simpledeformadd"
	bl_label = "Simple Deform (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'SIMPLE_DEFORM')
		self.report({'INFO'},'bpy.ops.modifier.simpledeformadd()')
		return {'FINISHED'}

class BsMax_OT_SMOOTH_Add(Operator):
	bl_idname = "modifier.smoothadd"
	bl_label = "Smooth (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'SMOOTH')
		self.report({'INFO'},'bpy.ops.modifier.smoothadd()')
		return {'FINISHED'}

class BsMax_OT_CORRECTIVE_SMOOTH_Add(Operator):
	bl_idname = "modifier.correctivesmoothadd"
	bl_label = "Corrective Smooth (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'CORRECTIVE_SMOOTH')
		self.report({'INFO'},'bpy.ops.modifier.correctivesmoothadd()')
		return {'FINISHED'}

class BsMax_OT_LAPLACIANSMOOTH_Add(Operator):
	bl_idname = "modifier.laplaciansmoothadd"
	bl_label = "Laplacian Smooth (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'LAPLACIANSMOOTH')
		self.report({'INFO'},'bpy.ops.modifier.laplaciansmoothadd()')
		return {'FINISHED'}

class BsMax_OT_SURFACE_DEFORM_Add(Operator):
	bl_idname = "modifier.surfacedeformadd"
	bl_label = "Surface Deform (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'SURFACE_DEFORM')
		self.report({'INFO'},'bpy.ops.modifier.surfacedeformadd()')
		return {'FINISHED'}

class BsMax_OT_WARP_Add(Operator):
	bl_idname = "modifier.warpadd"
	bl_label = "Warp (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'WARP')
		self.report({'INFO'},'bpy.ops.modifier.warpadd()')
		return {'FINISHED'}

class BsMax_OT_WAVE_Add(Operator):
	bl_idname = "modifier.waveadd"
	bl_label = "Wave (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'WAVE')
		self.report({'INFO'},'bpy.ops.modifier.waveadd()')
		return {'FINISHED'}

class BsMax_OT_CLOTH_Add(Operator):
	bl_idname = "modifier.clothadd"
	bl_label = "Cloth (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'CLOTH')
		self.report({'INFO'},'bpy.ops.modifier.clothadd()')
		return {'FINISHED'}

class BsMax_OT_COLLISION_Add(Operator):
	bl_idname = "modifier.collisionadd"
	bl_label = "Collision (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'COLLISION')
		self.report({'INFO'},'bpy.ops.modifier.collisionadd()')
		return {'FINISHED'}

class BsMax_OT_DYNAMIC_PAINT_Add(Operator):
	bl_idname = "modifier.dynamicpaintadd"
	bl_label = "Dynamic Paint (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'DYNAMIC_PAINT')
		self.report({'INFO'},'bpy.ops.modifier.dynamicpaintadd()')
		return {'FINISHED'}

class BsMax_OT_EXPLODE_Add(Operator):
	bl_idname = "modifier.explodeadd"
	bl_label = "Explode (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'EXPLODE')
		self.report({'INFO'},'bpy.ops.modifier.explodeadd()')
		return {'FINISHED'}

class BsMax_OT_FLUID_SIMULATION_Add(Operator):
	bl_idname = "modifier.fluidsimulationadd"
	bl_label = "Fluid Simulation (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'FLUID_SIMULATION')
		self.report({'INFO'},'bpy.ops.modifier.fluidsimulationadd()')
		return {'FINISHED'}

class BsMax_OT_OCEAN_Add(Operator):
	bl_idname = "modifier.oceanadd"
	bl_label = "Ocean (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'OCEAN')
		self.report({'INFO'},'bpy.ops.modifier.oceanadd()')
		return {'FINISHED'}

class BsMax_OT_PARTICLE_INSTANCE_Add(Operator):
	bl_idname = "modifier.particleinstanceadd"
	bl_label = "Particle Instance (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'PARTICLE_INSTANCE')
		self.report({'INFO'},'bpy.ops.modifier.particleinstanceadd()')
		return {'FINISHED'}

class BsMax_OT_PARTICLE_SYSTEM_Add(Operator):
	bl_idname = "modifier.particlesystemeadd"
	bl_label = "Particle System (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'PARTICLE_SYSTEM')
		self.report({'INFO'},'bpy.ops.modifier.particlesystemeadd()')
		return {'FINISHED'}

class BsMax_OT_SMOKE_Add(Operator):
	bl_idname = "modifier.smokeadd"
	bl_label = "Smoke (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'SMOKE')
		self.report({'INFO'},'bpy.ops.modifier.smokeadd()')
		return {'FINISHED'}

class BsMax_OT_SOFT_BODY_Add(Operator):
	bl_idname = "modifier.softbodyadd"
	bl_label = "Soft Body (add)"
	bl_options = {'REGISTER','UNDO'}
	@classmethod
	def poll(self, ctx):
		return is_objects_selected(ctx)
	def execute(self, ctx):
		modifier_add(ctx,ctx.selected_objects,'SOFT_BODY')
		self.report({'INFO'},'bpy.ops.modifier.softbodyadd()')
		return {'FINISHED'}

classes = [BsMax_OT_Lattice_2x2x2_Set,
		BsMax_OT_Lattice_3x3x3_Set,
		BsMax_OT_Lattice_4x4x4_Set,
		BsMax_OT_DATA_TRANSFER_Add,
		BsMax_OT_MESH_CACHE_Add,
		BsMax_OT_MESH_SEQUENCE_CACHE_Add,
		BsMax_OT_NORMAL_EDIT_Add,
		BsMax_OT_WEIGHTED_NORMAL_Add,
		BsMax_OT_UV_PROJECT_Add,
		BsMax_OT_UV_WARP_Add,
		BsMax_OT_VERTEX_WEIGHT_EDIT_Add,
		BsMax_OT_VERTEX_WEIGHT_MIX_Add,
		BsMax_OT_VERTEX_WEIGHT_PROXIMITY_Add,
		BsMax_OT_ARRAY_Add,
		BsMax_OT_BEVEL_Add,
		BsMax_OT_BOOLEAN_Add,
		BsMax_OT_BUILD_Add,
		BsMax_OT_DECIMATE_Add,
		BsMax_OT_EDGE_SPLIT_Add,
		BsMax_OT_Mask_Add,
		BsMax_OT_MIRROR_Add,
		BsMax_OT_MULTIRES_Add,
		BsMax_OT_REMESH_Add,
		BsMax_OT_Screw_Add,
		BsMax_OT_SKIN_Add,
		BsMax_OT_SOLIDIFY_Add,
		BsMax_OT_SUBSURF_Add,
		BsMax_OT_TRIANGULATE_Add,
		BsMax_OT_WIREFRAME_Add,
		BsMax_OT_ARMATURE_Add,
		BsMax_OT_CAST_Add,
		BsMax_OT_CURVE_Add,
		BsMax_OT_DISPLACE_Add,
		BsMax_OT_HOOK_Add,
		BsMax_OT_LAPLACIANDEFORM_Add,
		BsMax_OT_LATTICE_Add,
		BsMax_OT_MESH_DEFORM_Add,
		BsMax_OT_SHRINKWRAP_Add,
		BsMax_OT_SIMPLE_DEFORM_Add,
		BsMax_OT_SMOOTH_Add,
		BsMax_OT_CORRECTIVE_SMOOTH_Add,
		BsMax_OT_LAPLACIANSMOOTH_Add,
		BsMax_OT_SURFACE_DEFORM_Add,
		BsMax_OT_WARP_Add,
		BsMax_OT_WAVE_Add,
		BsMax_OT_CLOTH_Add,
		BsMax_OT_COLLISION_Add,
		BsMax_OT_DYNAMIC_PAINT_Add,
		BsMax_OT_EXPLODE_Add,
		BsMax_OT_FLUID_SIMULATION_Add,
		BsMax_OT_OCEAN_Add,
		BsMax_OT_PARTICLE_INSTANCE_Add,
		BsMax_OT_PARTICLE_SYSTEM_Add,
		BsMax_OT_SMOKE_Add,
		BsMax_OT_SOFT_BODY_Add]
		
def register_modifier():
	[bpy.utils.register_class(c) for c in classes]

def unregister_modifier():
	[bpy.utils.unregister_class(c) for c in classes]