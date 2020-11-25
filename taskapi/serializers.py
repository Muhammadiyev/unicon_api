from rest_framework import serializers
from .models import Draggable, DragandDrop, AddingColor


class AddingColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = AddingColor
        fields = ['id','backround','draganddrop','status','created_at']

class DragandDropSerializer(serializers.ModelSerializer):

    class Meta:
        model = DragandDrop
        fields = ['id','name','draggable', 'description','position', 'date','time','status','created_at']


class DragandDropListSerializer(serializers.ModelSerializer):
    color = AddingColorSerializer(read_only=True, many=True)
    id = serializers.IntegerField()
    
    class Meta:
        model = DragandDrop
        fields = ['id','name','draggable', 'description','position', 'color', 'date','time','status','created_at']


class DraggableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Draggable
        fields = ['id','name', 'status','created_at']


class DraggableListSerializer(serializers.ModelSerializer):
    drag_of_draggable = DragandDropListSerializer(many=True, required=False)
    id = serializers.IntegerField()

    class Meta:
        model = Draggable
        fields = ['id','name','drag_of_draggable', 'status','created_at']

    def update(self, instance, validated_data):
        drag_of_draggable_data = validated_data.pop('drag_of_draggable')
        for drag_of_draggable in drag_of_draggable_data:
            if 'id' in drag_of_draggable:
                parcel_id = drag_of_draggable.pop('id')
                DragandDrop.objects.update_or_create(id=parcel_id, defaults=drag_of_draggable)
            else:
                drag_of_draggable = Draggable.objects.create(**drag_of_draggable)
                instance.drag_of_draggable.add(drag_of_draggable)
   
        return super(DraggableListSerializer, self).update(instance, validated_data)

    