from call.models import Assign

def call__on_post_save(instance: Assign, created: bool, **kwargs):
    if created:
        message_type = "call.assign.waiting"
    else:
        if instance.status == 'success':
            message_type = "call.assign.success"
        elif instance.status == 'riding':
            message_type = "call.assign.riding"
        elif instance.status == 'finish':
            message_type = "call.assign.finish"        
        else:
            message_type = "call.assign.finish"

    assign_pk = instance.pk

    instance.channel_layer_group_send(
        Assign.make_call_group_name(assign_pk),
        {
        "type": message_type,
        "assign_id": assign_pk,
    })

def call__on_post_delete(instance: Assign, **kwargs):
    assign_pk = instance.pk

    instance.channel_layer_group_send(
        Assign.make_call_group_name(assign_pk),
        {
        "type": "call.assign.deleted",
        "post_id": assign_pk,
    })
