import os
from box.exceptions import BoxValueError
import yaml
from text_summerizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yml(path_to_yaml: Path) -> ConfigBox:
    
    """_summary_

    Args:
        path_to_yaml (str): path to yaml file
        
    Rises:
        ValueError: if yaml file is empty
        e: empty yaml file    

    Returns:
        ConfigBox: configbox type
    """
    
    with open(path_to_yaml) as yaml_file:
        
        try:
            content = yaml.safe_load(yaml_file)
            
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            
            return ConfigBox(content)
        
        except BoxValueError:
            
            raise ValueError(f"yaml file: {path_to_yaml} is empty")
        
        except Exception as e:
            
            raise e
        
   



@ensure_annotations
def create_directories(paths_to_create: list, verbose=True):
    """_summary_

    Args:
        paths_to_create (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs are to be created. Defaults to False.
        
    Returns:
        None
    """
    for path in paths_to_create:
        
        os.makedirs(path, exist_ok=True)
        
        if verbose:
            logger.info(f"created directory at: {path}")
            
            
            
@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    
    Args:
        path (Path): path of the file
        
    Returns:
        str: size of the file

    """           
    
    size_in_kb = round(os.path.getsize(path)/1024)
    
    return f"~ {size_in_kb} KB"