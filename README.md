# HavocsCall's ComfyUI Custom Nodes
Some quality of life nodes for ComfyUI.
## Installation
### Recommended
Install with ComfyUI manager
### Manual
Clone with git into your custom_nodes folder
```
git clone https://github.com/HavocsCall/comfyui_HavocsCall_Custom_Nodes.git
```  
## Features
### Basic Nodes
- Float Selector - Returns the given `FLOAT`, unmodified.
- Integer Selector - Returns the given `INTEGER`, unmodified.
- Prompt Combiner - Combines the given prompts into a single string, separated by commas.
- Sampler Config - One node for most, if not all, KSampler inputs.
- Save Image - A Save image node with a separate input for folder and a toggle for saving the metadata.
- Text Box - Returns the given `STRING`, unmodified.
### Conversion Nodes
- Float to Integer - Converts a `FLOAT` to an `INT`. (Note: This truncates towards zero, it does not round)
- Float to String - Converts a `FLOAT` to a `STRING`.
- Integer to Float - Converts an `INTEGER` to a `FLOAT`.
- Integer to String - Converts an `INTEGER` to a `STRING`.
- String to Float - Converts a `STRING` to a `FLOAT`. (Returns 0 if an invalid `STRING`)
- String to Integer - Converts a `STRING` to a `INT`. (Returns 0.0 if an invalid `STRING`)
### Math Nodes
- Math Operation - Run math operations on an input number
### Prompt Styler Node
- Prompt Styler - Adds text to your prompts based on json files. - See [Prompt Styler Nodes](https://github.com/HavocsCall/ComfyUI_HavocsCall_Custom_Nodes/wiki/Prompt-Styler-Nodes) for more information.
### Switch Nodes
- Clip Switch - Switches between two `CLIPS`.
- Conditioning Switch - Switches between two `CONDITIONING`.
- Image Switch - Switches between two `IMAGES`.
- Latent Switch - Switches between two `LATENTS`.
- Model Switch - Switches between two `MODELS`.
- String Switch - Switches between two `STRINGS`.
- VAE Switch - Switches between two `VAE`.
## Comfy Registry
https://registry.comfy.org/nodes/havocscall_custom_nodes
