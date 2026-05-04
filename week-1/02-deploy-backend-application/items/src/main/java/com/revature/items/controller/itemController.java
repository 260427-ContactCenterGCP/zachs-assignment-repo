package com.revature.items.controller;

import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
public class itemController {

    private final List<String> items = new ArrayList<>();

    @GetMapping("/items")
    public List<String> getItems(){return items;}

    @GetMapping("/items/{id}")
    public String getItemById(@PathVariable int id){
        return items.get(id);
    }

    @PostMapping("/items")
    public String addItem(@RequestBody String item){
        System.out.println("Added " + item + "to list");
        items.add(item);
        return item;
    }

    @PutMapping("items/{id}")
    public String putItem(@RequestBody String item, @PathVariable int id){
        System.out.println("Changed to " + item);
        items.set(id, item);
        return item;
    }

    @DeleteMapping("items/{id}")
    public String removeItem(@PathVariable int id){
        String item = items.remove(id);
        return ("Removed " + item + " from list");
    }
}
