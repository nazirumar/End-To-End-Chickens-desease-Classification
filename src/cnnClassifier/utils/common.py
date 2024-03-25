import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a yaml file and returns

    Args:
        path_to_yaml (Path): Path like input

    Raises:
    
        ValueError: Raised when yaml file is empty
        ValueError: Raised when yaml file is invalid

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError("yaml file is empty ")
    except Exception as e:
        raise e



def create_directories(path_to_directories: list, verbose=True):
    """Create directories

    Args:
        path_to_directories (list): List of directories to be created
        verbose (bool, optional): [description]. Defaults to True.

    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Creating Directory; {path}")
        

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save json data

    Args:
        path (Path): Path like input
        data (dict, optional): [description]. Defaults to {}.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file: {path} saved successfully")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load json data

    Args:
        path (Path): Path to json file

    Returns:
        ConfigBox: ConfigBox type
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from : {path}")
    return ConfigBox(content)



def save_bin(data: Any, path: Path):
    """Save binary file 

    Args:
        data (Any): Data to be saved as binary
        path (Path): Path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")
    

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary data

    Args:
        path (Path): Path to binary file

    Returns:
        Any: Object stored in the file
    """
    data =  joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Get size in kb

    Args:
        path (Path): Path of the file
    
    Returns:
    
        str: Size in kb
    """
    size = round(os.path.getsize(path) / 1024)
    return f"{size:.2f} kb"

def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, "wb") as f:
        f.write(imgdata)
        logger.info(f"image file saved at: {filename}")
        f.close()


def encodeImageIntoBase64(cropedImagePath):
    with open(cropedImagePath, "rb") as image_file:
        return base64.b64encode( image_file.read())