# HavocsCall's Custom ComfyUI Nodes

Some quality of life nodes for ComfyUI.
## Installation

Clone with git into your custom_nodes folder
```
git clone https://github.com/HavocsCall/comfyui_HavocsCall_Custom_Nodes.git
```
## Features
### Basic Nodes
- Float Selector - Returns the given `FLOAT`, unmodified.
- Int Selector - Returns the given `INTEGER`, unmodified.
- Prompt Combiner - Combines the given prompts into a single string, separated by commas.
- Sampler Config - One node for most, if not all, KSampler inputs.
- Text Box - Returns the given `STRING`, unmodified.

### Conversion Nodes
- Float to Int - Rounds the given `FLOAT` to the nearest whole number and returns it as an `INTEGER`.
- Float to String - Converts a `FLOAT` to a `STRING`.
- Int to Float - Converts an `INTEGER` to a `FLOAT`.
- Int to String - Converts an `INTEGER` to a `STRING`.

### Prompt Styler Nodes
- json based Prompt Styler - Create a .json file in the `Styler_Data` folder formatted like this:
```json
[
    {
        "name": "None",
        "positive_prompt": "{prompt}",
        "negative_prompt": "{prompt}"
    },
    {
        "name": "Example",
        "positive_prompt": "{prompt}, Example",
        "negative_prompt": "Example, {prompt}"
    },
    {
        etc...
    }
]
```
Each .json file will create it's own node with the name of the .json file + Styler.

### Switch Nodes
- Clip Switch - Switches between two `CLIPS`.
- Conditioning Switch - Switches between two `CONDITIONING`.
- Image Switch - Switches between two `IMAGES`.
- Latent Switch - Switches between two `LATENTS`.
- Model Switch - Switches between two `MODELS`.
- String Switch - Switches between two `STRINGS`.
- VAE Switch - Switches between two `VAE`.