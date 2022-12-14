import coreapi
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import renderers, response

schema = coreapi.Document(
 title='Sample API',
 content={
     'sample': coreapi.Link(
         url='/sample/',
         action='post',
         fields=[
             coreapi.Field(
                name='from',
                required=True,
                location='query',
                description='City name or airport code.'
            ),
            coreapi.Field(
                name='to',
                required=True,
                location='query',
                description='City name or airport code.'
            ),
            coreapi.Field(
                name='date',
                required=True,
                location='query',
                description='Flight date in "YYYY-MM-DD" format.'
            )
        ],
        description='Create partner'
    )
   }
 )

@api_view()
@renderer_classes([renderers.CoreJSONRenderer])
def schema_view(request):
    return response.Response(schema)