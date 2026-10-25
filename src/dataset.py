import os
import torch
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import torchvision.transforms as T

class FachadasDataset(Dataset):
    """
    Dataset unificado para restauración supervisada de fachadas.
    Retorna pares alineados:
      - 'source': Imagen con degradación sintética (Input para el modelo)
      - 'target': Imagen limpia original (Ground Truth de referencia)
      - 'prompt': Descripción textual genérica para modelos de difusión (SDXL / SD3)
    """
    def __init__(self, raiz_split, tamano=(512, 512), 
                 prompt="A high-resolution photograph of a restored historic architectural building facade, clean masonry"):
        self.dir_source = os.path.join(raiz_split, 'source')
        self.dir_target = os.path.join(raiz_split, 'target')
        
        # Listar únicamente archivos de imagen válidos
        exts = ('.jpg', '.jpeg', '.png', '.bmp')
        self.archivos = sorted([
            f for f in os.listdir(self.dir_source) 
            if f.lower().endswith(exts)
        ])
        self.prompt = prompt
        
        # Transformaciones estándar para normalización en rango [-1, 1]
        self.transform = T.Compose([
            T.Resize(tamano),
            T.CenterCrop(tamano),
            T.ToTensor(),
            T.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
        ])

    def __len__(self):
        return len(self.archivos)

    def __getitem__(self, idx):
        nombre_archivo = self.archivos[idx]
        
        ruta_source = os.path.join(self.dir_source, nombre_archivo)
        ruta_target = os.path.join(self.dir_target, nombre_archivo)
        
        img_source = Image.open(ruta_source).convert('RGB')
        img_target = Image.open(ruta_target).convert('RGB')
        
        return {
            "source": self.transform(img_source),   # Tensor (3, H, W) en [-1, 1]
            "target": self.transform(img_target),   # Tensor (3, H, W) en [-1, 1]
            "prompt": self.prompt,
            "filename": nombre_archivo
        }

def obtener_dataloader(raiz_split, batch_size=4, shuffle=True, tamano=(512, 512), num_workers=2):
    """
    Función utilitaria para instanciar el DataLoader directamente.
    """
    dataset = FachadasDataset(raiz_split=raiz_split, tamano=tamano)
    loader = DataLoader(
        dataset, 
        batch_size=batch_size, 
        shuffle=shuffle, 
        num_workers=num_workers,
        pin_memory=True
    )
    return loader# Dataset y Dataloader unificado para entrenamiento
