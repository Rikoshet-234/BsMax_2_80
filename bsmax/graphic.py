
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

import bpy, bgl, gpu
from gpu_extras.batch import batch_for_shader
from bpy_extras.view3d_utils import location_3d_to_region_2d

def get_screen_pos(ctx,coord):
	region = ctx.region
	rv3d = ctx.space_data.region_3d
	return location_3d_to_region_2d(region, rv3d, coord, default=None)

def draw_line(self,mode,color):
	bgl.glEnable(bgl.GL_BLEND)
	coords = [self.start, self.end]
	shader = gpu.shader.from_builtin(mode)
	batch = batch_for_shader(shader, 'LINE_STRIP', {"pos": coords})
	shader.bind()
	shader.uniform_float("color", color)
	batch.draw(shader)
	bgl.glDisable(bgl.GL_BLEND)

def register_line(ctx,self,mode,color):
	""" owner most have to "start" and "end" point values """
	""" self.start self.end """
	space = ctx.area.spaces.active
	if mode == '2d':
		return space.draw_handler_add(draw_line,tuple([self,'2D_UNIFORM_COLOR',color]),'WINDOW','POST_PIXEL')
	if mode == '3d':
		return space.draw_handler_add(draw_line,tuple([self,'3D_UNIFORM_COLOR',color]),'WINDOW','POST_VIEW')

def unregister_line(handle):
	if handle != None:
		bpy.types.SpaceView3D.draw_handler_remove(handle,'WINDOW')