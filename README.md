<h1>ViLT FastAPI</h1>
<p>An basic fastapi app made following a tutorial by Patrick Loeber. </p>
<p>The ViLT model is the ViLT b32 fine tuned vqa model from hugging face that uses pytorch. The model that can process both images and text. When the user gives the api a question and an image the api will return an answer to that question. </p>
<p>Deviverable: A REST API connected to a ViLT model that lives in a docker container. </p>

<h3>Project Elements:</h3>
<ul>
  <li>
    <h3>ViLT Model</h3>
    <p><b>Description: </b>Using the processor and model provided by hugging face, the function takes a text and an image. Using the model then answers the question asked about the picture. </p>
    <p><b>Location: </b>model.py</p>
  </li>
  <li>
    <h3>REST API</h3>
    <p><b>Description: </b>A basic FastAPI app with the ability to deliver the model with a string and an image. </p>
    <p><b>Location: </b>main.py</p>
  </li>
  <li>
    <h3>Docker File</h3>
    <p><b>Description: </b>The API can be ran using a python based image. The container is open on port 8000. </p>
    <p><b>Location: </b>Dockerfile</p>
  </li>
</ul>
