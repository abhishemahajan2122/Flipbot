from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2
import random

PAT = 'a050a9503f02459f924173b12cf8bb1a'
USER_ID = 'clarifai'
APP_ID = 'main'
MODEL_ID = 'apparel-classification-v2'
MODEL_VERSION_ID = '651c5412d53c408fa3b4fe3dcc060be7'

channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)

metadata = (('authorization', 'Key ' + PAT),)

userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)
list=[]

with open('output.txt', 'r') as file:
    image_urls = file.readlines()

for IMAGE_URL in image_urls:
    IMAGE_URL = IMAGE_URL.strip()

    post_model_outputs_response = stub.PostModelOutputs(
        service_pb2.PostModelOutputsRequest(
            user_app_id=userDataObject,
            model_id=MODEL_ID,
            version_id=MODEL_VERSION_ID,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        image=resources_pb2.Image(
                            url=IMAGE_URL
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
        print(post_model_outputs_response.status)
        raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

    output = post_model_outputs_response.outputs[0]
    # print("Predicted concepts:")
    cnt=0
    # print("The person is wearing the following : ")
    for concept in output.data.concepts:
        # print(f" {concept.name}")
        list.append(concept.name)
        # print("%s %.2f" % (concept.name, concept.value))
        # if(int(concept.value)>=45):
        #     list.append(concept.name)
        cnt+=1
        if(cnt==5):
            break
    
print(list)

#k=5  This is changed according to user's comfort
selected_entries = random.sample(list, 5)  # Randomly select 5 entries

with open('final_prompt.txt', 'w') as file:
    for entry in selected_entries:
        file.write(entry + '\n')

print("Selected entries written to 'final_prompt.txt'")


# print(output)
