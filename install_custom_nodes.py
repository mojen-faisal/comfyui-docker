import subprocess

NODES = [
"comfyui-ollama",
"comfyui-lama-remover",
"comfyui-dynamicprompts",
"comfyui-ollama-llms",
"sdxl-recommended-res-calc",
"ComfyUI_VisualStylePrompting",
"ComfyUI-KJNodes",
"OneButtonPrompt",
"was-node-suite-comfyui",
"ComfyUI-Miaoshouai-Tagger",
"ComfyUI_LayerStyle",
"ComfyUI-Easy-Use",
"rgthree-comfy",
"ComfyUI_JPS-Nodes",
"ComfyUI_Comfyroll_CustomNodes",
"comfy-plasma",
"ComfyUI-Impact-Pack",
"ComfyUI_essentials",
"comfyui-prompt-composer"
]

def install_custom_nodes(nodes):
  print(f"Installing nodes: {nodes}")
  for node in nodes:
    if "comfyui-lama-remover" in node:
      cmd = f"git clone https://github.com/Layer-norm/comfyui-lama-remover.git /root/comfy/ComfyUI/custom_nodes/comfyui-lama-remover"
    else:
      cmd = f"comfy node install {node}"
    subprocess.run(cmd, shell=True, check=True)
    print(f"Installed node: {node}")
  
  if "ComfyUI-Anyline" in nodes:
    subprocess.run("sed -i 's/src.controlnet_aux/src.custom_controlnet_aux/g' /root/comfy/ComfyUI/custom_nodes/ComfyUI-Anyline/anyline.py", shell=True)
    print(f"Fixed ComfyUI-Anyline import")

if __name__ == "__main__":
  install_custom_nodes(NODES)